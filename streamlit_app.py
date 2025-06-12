import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="지역별 범죄 지도", layout="wide")
st.title("📍 지역별 범죄 발생 지도")

# CSV 데이터 불러오기
df = pd.read_csv("crime_data.csv", encoding="euc-kr")


# 지도 초기 위치 (서울 기준)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# 각 지역 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        popup=(
            f"<b>{row['지역']}</b><br>"
            f"살인: {row['살인']}<br>"
            f"강도: {row['강도']}<br>"
            f"강간: {row['강간']}<br>"
            f"절도: {row['절도']}<br>"
            f"폭력: {row['폭력']}"
        )
    ).add_to(m)

# Streamlit에 folium 지도 렌더링
folium_static(m)
