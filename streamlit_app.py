import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="전국 범죄 발생 분석", layout="wide")

st.title("📊 전국 범죄 발생 분석 대시보드")
st.markdown("데이터 출처: 경찰청 / 범죄유형별 지역별 발생 건수")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv('crime_data.csv', encoding='euc-kr')  # utf-8 오류 시 euc-kr로
    return df

df = load_data()

# 데이터 구조 변환: wide → long
df_long = pd.melt(df, id_vars=['범죄대분류', '범죄중분류'], var_name='지역', value_name='건수')

# 사이드바: 필터 설정
범죄대분류_options = df_long['범죄대분류'].unique()
선택_범죄대분류 = st.sidebar.selectbox("범죄 대분류 선택", options=범죄대분류_options)

df_filtered = df_long[df_long['범죄대분류'] == 선택_범죄대분류]

범죄중분류_options = df_filtered['범죄중분류'].unique()
선택_범죄중분류 = st.sidebar.selectbox("범죄 중분류 선택", options=범죄중분류_options)

df_filtered = df_filtered[df_filtered['범죄중분류'] == 선택_범죄중분류]

# 상단 요약
총건수 = df_filtered['건수'].sum()
st.metric(label="총 발생 건수", value=f"{총건수:,} 건")

# 바 차트 시각화
fig = px.bar(df_filtered.sort_values('건수', ascending=False), 
             x='건수', y='지역', orientation='h',
             title=f"{선택_범죄대분류} > {선택_범죄중분류} 발생 현황",
             labels={'건수': '건수', '지역': '지역'},
             color='건수', color_continuous_scale='Reds')

st.plotly_chart(fig, use_container_width=True)

# 원시 데이터 확인 옵션
with st.expander("🔍 원시 데이터 보기"):
    st.dataframe(df_filtered.reset_index(drop=True))
