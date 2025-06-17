import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 부산 동별 범죄 발생률 시각화")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 또는 Excel 파일 업로드", type=["csv", "xlsx"])

if uploaded_file is not None:
    # CSV 또는 엑셀 읽기
    if uploaded_file.name.endswith('busan.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # 필요한 열 이름: "동이름", "범죄발생률" (예시)
    st.subheader("원본 데이터")
    st.dataframe(df)

    # 범죄율 기준 정렬
    df_sorted = df.sort_values(by="범죄발생률", ascending=True)

    # 그래프 그리기
    st.subheader("📉 범죄 발생률 (낮은 순)")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df_sorted["동이름"], df_sorted["범죄발생률"], color='salmon')
    ax.set_xlabel("범죄 발생률")
    ax.set_ylabel("부산 동이름")
    ax.set_title("부산 동별 범죄 발생률")
    st.pyplot(fig)

    # 가장 낮은 동 이름
    safest = df_sorted.iloc[0]
    st.success(f"✅ 범죄 발생률이 가장 낮은 지역: **{safest['동이름']}** ({safest['범죄발생률']})")
