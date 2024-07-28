import crawler as crawler
import preprocess as preprocess
import model as model

def main():
    print("연금복권 번호 추천 프로그램을 시작합니다.")
    currentVersion = crawler.crawlData()
    seriesWeight, numbersWeight = preprocess.preprocessData(currentVersion)
    print(f"추천 복권 번호: {model.KMeansModel(seriesWeight)[0]}조", ' '.join([str(i) for i in model.KMeansModel(numbersWeight)]))
    print("연금복권 번호 추천 프로그램을 종료합니다.")

if __name__ == "__main__":
    main()