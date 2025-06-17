import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 부산 동별 범죄율 시각화")

uploaded_file = st.file_uploader("busan.csv)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("✅ 데이터 로드 성공!")
        st.write(f"데이터 크기: {df.shape}")
        st.dataframe(df)

        # 컬럼명 공백 제거 및 소문자 변환(엑셀에서 저장할 때 공백 문제 대비)
        df.columns = df.columns.str.strip()

        if "동이름" in df.columns and "범죄율" in df.columns:
            st.write("✅ '동이름'과 '범죄율' 컬럼 확인 완료")

            # 범죄율 컬럼 숫자 타입 변환 시도 (문자열로 저장됐을 수 있음)
            df["범죄율"] = pd.to_numeric(df["범죄율"], errors='coerce')
            if df["범죄율"].isnull().any():
                st.warning("⚠️ '범죄율' 컬럼에 숫자가 아닌 값이 포함되어 있어 일부가 NaN 처리되었습니다.")

            # 그래프 그리기
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(df["동이름"], df["범죄율"], color='orange')
            ax.set_title("부산 동별 범죄율")
            ax.set_xlabel("동이름")
            ax.set_ylabel("범죄율")
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig)

            # 범죄율 통계 간단히 보여주기
            st.write("### 범죄율 요약 통계")
            st.write(df["범죄율"].describe())

        else:
            st.error("❌ '동이름' 또는 '범죄율' 컬럼이 CSV 파일에 없습니다. 컬럼 이름을 확인해주세요.")

    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("CSV 파일을 업로드해주세요.")
