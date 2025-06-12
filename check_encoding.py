import pandas as pd

# 원본 CSV 불러오기
df = pd.read_csv('crime_data.csv', encoding='utf-8')

# 긴 형태로 변환
df_melt = pd.melt(df, id_vars=['범죄대분류', '범죄중분류'], var_name='지역명', value_name='발생건수')

# 결과 확인
print(df_melt.head())

# 필요시 새 CSV로 저장
df_melt.to_csv('crime_data_long.csv', index=False)
