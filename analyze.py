import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('crime_data.csv', encoding='euc-kr')

# 컬럼명 확인
print("컬럼명 목록:")
print(df.columns.tolist())

# 데이터 일부 확인
print("\n데이터 미리 보기:")
print(df.head())
