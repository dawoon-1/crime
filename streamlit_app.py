import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기
df = pd.read_csv("부산동별경찰서.csv", encoding='euc-kr')

# 제목
st.title("부산 동별 경찰서 개수 시각화")

# 막대그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["경찰서"], df["개수"], color='skyblue')  # '경찰서명' → '경찰서'로 변경
ax.set_xlabel("경찰서")
ax.set_ylabel("개수")
ax.set_title("부산 경찰서별 개수")
plt.xticks(rotation=45, ha='right')

# 그래프 출력
st.pyplot(fig)
