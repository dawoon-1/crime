import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('year_data.csv')

# 그래프 크기 설정
plt.figure(figsize=(12, 6))

# 선 그래프 그리기
plt.plot(df['년도'], df['전체형법범죄'], label='전체형법범죄')
plt.plot(df['년도'], df['살인'], label='살인')
plt.plot(df['년도'], df['강도'], label='강도')
plt.plot(df['년도'], df['성폭력'], label='성폭력(강간 포함)')
plt.plot(df['년도'], df['폭행'], label='폭행')
plt.plot(df['년도'], df['절도'], label='절도')

# 그래프 제목 및 축 라벨 설정
plt.title('주요 범죄 유형별 추이 (2012-2023)')
plt.xlabel('년도')
plt.ylabel('범죄 발생 건수 / 비율')

# 범례 추가
plt.legend()

# 그리드 추가
plt.grid(True)

# 그래프 출력
plt.show()
