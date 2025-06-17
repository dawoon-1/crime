import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="부산 5대 범죄 시각화", layout="wide")

st.title("📊 부산 동별 5대 범죄 통계 시각화")
st.write("엑셀 또는 CSV 파일을 업로드하여 범죄 평균을 기준으로 시각화합니다.")

# 1. 파일 업로드
uploaded_file = st.file_uploader("CSV 또는 엑셀 파일 업로드", type=["csv", "xlsx"])

if uploaded_file is not None:
    # 2. 파일 확장자에 따라 판다스로 읽기
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # 3. 데이터 미리보기
    st.subheader("원본 데이터 미리보기")
    st.dataframe(df)

    # 4. 평균 기준으로 정렬
    try:
        df_sorted = df.sort_values(by='평균', ascending=True)
    except KeyError:
        st.error("⚠️ '평균'이라는 열이 존재하지 않습니다. 파일에 평균 열을 포함해주세요.")
        st.stop()

    # 5. 시각화: 막대그래프
    st.subheader("📉 평균 범죄율 막대그래프")

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(df_sorted['동이름'], df_sorted['평균'], color='skyblue')
    ax.set_xlabel('평균 범죄 건수')
    ax.set_ylabel('동 이름')
    ax.set_title('부산 동별 평균 범죄율')

    # 값 표시
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width:.1f}', va='center')

    st.pyplot(fig)

    # 6. 가장 안전한 동 표시
    safest = df_sorted.iloc[0]
    st.success(f"✅ **가장 안전한 동**은 **{safest['동이름']}**입니다. (평균 범죄율: {safest['평균']:.1f})")
