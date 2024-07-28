from sklearn.cluster import KMeans
import random


def recommend_numbers(cluster_centers):
    # 클러스터 중심 중 하나를 무작위로 선택
    recommended_set = random.choice(cluster_centers)
    return recommended_set

def KMeansModel(arr):
    # 데이터 전처리: 복권 번호를 행렬 형태로 변환

    # K-means 클러스터링 모델 생성 및 학습
    kmeans = KMeans(n_clusters=5, random_state=0)
    kmeans.fit(arr)

    # 각 클러스터의 중심 좌표 (대표 번호 세트) 추출
    cluster_centers = kmeans.cluster_centers_.astype(int)
    recommended_numbers = recommend_numbers(cluster_centers)
    
    return recommended_numbers