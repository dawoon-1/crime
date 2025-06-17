import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 부산 동별 범죄율 시각화 테스트")

uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ 데이터 모양:", df.shape)
    st.dataframe(df)

    if "동이름" in df.columns and "범죄율" in df.columns:
        st.write("✅ 그래프 그리는 중...")
        fig, ax = plt.subplots()
        ax.bar(df["동이름"], df["범죄율"], color='orange')
        ax.set_title("부산 동별 범죄율")
        ax.set_xlabel("동이름")
        ax.set_ylabel("범죄율")
        st.pyplot(fig)
    else:
        st.error("❌ '동이름' 또는 '범죄율'이라는 열 이름이 없습니다.")
