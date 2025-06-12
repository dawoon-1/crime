import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('crime_data.csv', encoding='utf-8')  # 혹시 에러나면 encoding='cp949'로 바꿔보세요

# 데이터 구조 확인
print(df.head())         # 처음 5행 출력
print(df.columns.tolist())  # 컬럼 이름 출력
