import numpy as np
import pandas as pd

def checkData(df):
    try:
        # null 값 확인
        nullDataNum = df.apply(lambda row: row.astype(str).str.contains('\[\]').any(), axis=1).sum()
        if  nullDataNum > 0:
            print(f"Error Null data({nullDataNum} row) included!")
        else:
            return df
    except Exception as e:
        print(f"Error during preprocessing: {e}")

# 최근 당첨 내역에 대한 가중치 부여
def getWeight(df):
    weights = np.arange(1, len(df) + 1)

    expanded_data = []
    for i, weight in enumerate(weights):
        for _ in range(weight):
            expanded_data.append(df.iloc[i].values)
    expanded_data = np.array(expanded_data)
    
    return expanded_data


def preprocessData(df):
    # 데이터 확인
    checked = checkData(df)

    # 데이터 리스트 to 개별 데이터
    for i in range(1, 7):
        checked[f'당첨번호{i}'] = checked['당첨번호 리스트'].apply(lambda x: int(x[i-1]))
        
    # '당첨번호 리스트' 컬럼 제거
    data = checked.drop(columns=['당첨번호 리스트'])
    
    # 조, 당첨번호 구분
    series = data[['조']]
    numbers = data[['당첨번호1','당첨번호2','당첨번호3','당첨번호4','당첨번호5','당첨번호6']]
    
    # 가중치 구버전
    # weights = np.linspace(1, 0, len(data), endpoint=False)
    # for i in range(1, 7):
    #     data['조 가중치'] = data['조'].map(data['조'].value_counts() / len(data))
    #     data[f'당첨번호{i} 가중치'] = data[f'당첨번호{i}'].map(data[f'당첨번호{i}'].value_counts() / len(data))
        

    # 번호별 당첨 가중치 반영한 데이터 확장
    seriesWeight = getWeight(series)
    numbersWeight = getWeight(numbers)

    return seriesWeight, numbersWeight