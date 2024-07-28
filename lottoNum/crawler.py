# 라이브러리
import numpy as np
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException


# 크롬 윈도우 설정
def open_chrome():
    try:
        # 크롬 옵션
        option = webdriver.ChromeOptions()
        option.add_argument("--window-size=800,1400")   # 크롬 윈도우 사이즈 조절

        # selenium 버전 4.0 이상이면 별도의 Chrome driver 설치 필요 없음
        driver = webdriver.Chrome(options=option) 

        return driver
    except WebDriverException as e:
        print(f"Error opening Chrome: {e}")
        raise



# 보유하고 있는 가장 마지막 회차 번호 추출
def findLastNum():
    try:
        # 이전 csv 파일 불러오기
        latestFile = sorted(os.listdir('./data'))[-1]
        tempDataframe = pd.read_csv(f'./data/{latestFile}')
        print(f"보유하고 있는 최신 회차는 {tempDataframe['회차'].iloc[0]}회 입니다.")
        return tempDataframe['회차'].iloc[0]

    except Exception as e:
        print(f"Error finding last number: {e}\nstart at num = 1")
        return 1


def getData(gameResult, driver):
    try:
        # 당첨번호
        numList = [int(driver.find_element(By.XPATH, f'//*[@id="tab_pension720"]/div[2]/div[1]/ul/li[{i}]').text) for i in range(1,7)]
        
        # 각 데이터 추가
        gameResult['회차'].append(int((driver.find_element(By.XPATH, '//*[@id="tab_pension720"]/div[1]/h2/strong').text)[:-1]))
        gameResult['조'].append(int(driver.find_element(By.XPATH, '//*[@id="tab_pension720"]/div[2]/div[1]/h4/strong').text))
        gameResult['당첨번호 리스트'].append(numList)

    except NoSuchElementException as e:
        print(f"Error extracting data: {e}")


# csv 파일 최신화
def merge_csv(currentVersion):
    try:
        # 오늘 날짜
        today = time.strftime('%Y%m%d') 

        # csv 파일 목록 불러오기
        latestFile = sorted(os.listdir('./data'))
        
        # 이전에 저장한 파일이 있을 경우
        if latestFile != []:    
            latestDate = latestFile[-1][-12:-4]
            
            # 같은 날 다시 크롤링한 경우 
            if latestDate == today:
                latestDate = latestFile[-2][-12:-4]
             
            latestVersion = pd.read_csv(f'./data/gameResult_{latestDate}.csv')

            # 데이터 프레임 병합
            currentVersion = pd.concat([latestVersion,currentVersion], ignore_index=True)
            currentVersion = currentVersion.sort_values(by='회차', ascending=False)
        else:
            pass
        # csv 파일로 저장
        currentVersion.to_csv(f'./data/gameResult_{today}.csv', encoding='utf-8-sig', index = False)
            
    except Exception as e:
        print(f"Error merging CSV: {e}")


# 연금복권 데이터 크롤링
def crawlData():
    # 사용할 변수 정의
    driver = open_chrome()
    lastNum = findLastNum()
    gameResult = {'회차': [], '조':[], '당첨번호 리스트': []}

    try:
        # 최신 회차 정보 가져오기
        url = "https://m.dhlottery.co.kr/gameResult.do?method=win720"
        driver.get(url)
        num = int((driver.find_element(By.XPATH, '//*[@id="tab_pension720"]/div[1]/h2/strong').text)[:-1])
        driver.implicitly_wait(time_to_wait=10)

        # 크롤링
        if num != lastNum+1:    # 가장 최신회차만 크롤링 필요한지 판단
            for i in range(num,lastNum-1,-1):
                url = f"https://m.dhlottery.co.kr/gameResult.do?method=win720&Round={i}"
                driver.get(url) 
                getData(gameResult, driver)
                time.sleep(np.random.randint(3))
        else:
            getData(gameResult, driver)
    except Exception as e:
        print(f"Error during crawling: {e}")

    finally:
        # 크롬창 닫기
        driver.quit()

    # 데이터 프레임 화
    currentVersion = pd.DataFrame(gameResult)
    
    # csv 파일로 저장 및 최신화
    merge_csv(currentVersion)

    return currentVersion