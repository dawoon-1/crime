import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 부산 동별 범죄율 시각화")

# CSV 파일 경로를 직접 지정
csv_path = "busan.csv"  # 여기에 본인의 CSV 파일 경로 넣으세요

try:
    df = pd.read_csv(csv_path)
    st.write("✅ 데이터 로드 성공!")
    st.write(f"데이터 크기: {df.shape}")
    st.dataframe(df)

    df.columns = df.columns.str.strip()  # 컬럼명 공백 제거

    if "동이름" in df.columns and "범죄율" in df.columns:
        df["범죄율"] = pd.to_numeric(df["범죄율"], errors='coerce')
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(df["동이름"], df["범죄율"], color='orange')
        ax.set_title("부산 동별 범죄율")
        ax.set_xlabel("동이름")
        ax.set_ylabel("범죄율")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

        st.write("### 범죄율 요약 통계")
        st.write(df["범죄율"].describe())

    else:
        st.error("❌ '동이름' 또는 '범죄율' 컬럼이 없습니다.")

except Exception as e:
    st.error(f"파일을 읽는 중 오류 발생: {e}")
