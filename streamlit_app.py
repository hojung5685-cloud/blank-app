st.title("🚗 주차 후보 찾기")
st.write("가게 이름과 지역을 넣으면 주변 주차 후보를 어떻게 찾을지 보여준다.")

store_name = st.text_input("가게 이름", placeholder="예: 스타벅스")
location = st.text_input("지역", placeholder="예: 대구 수성구")

if st.button("검색"):
    if not store_name or not location:
        st.warning("가게 이름과 지역을 둘 다 입력해라.")
    else:
        st.success(f"{location}에 있는 {store_name} 주변 주차 후보를 찾는 중")

        st.subheader("추천 방식")
        st.write("1. 반경 300m 안 공영주차장 찾기")
        st.write("2. 없으면 민영주차장 찾기")
        st.write("3. 도보 5분 이내 후보 우선 보기")

        st.subheader("AI 요약")
        st.write(
            f"'{location}'의 '{store_name}' 주변은 공영주차장을 먼저 보고, "
            "없으면 가까운 민영주차장을 보는 방식이 가장 현실적이다."
        )