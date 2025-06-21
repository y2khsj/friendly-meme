import streamlit as st

# 🎨 앱 제목 및 설명
st.markdown("<h1 style='text-align: center; color: purple;'>🌟 MBTI 진로 추천기 🌟</h1>", unsafe_allow_html=True)
st.markdown("당신의 성격 유형에 딱 맞는 <span style='color:orange;'>직업</span>을 추천해드릴게요! 🤩", unsafe_allow_html=True)
st.markdown("---")

# 🔮 MBTI 리스트
mbti_list = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 📊 MBTI별 추천 직업 데이터
job_dict = {
    'INTJ': ['🧠 데이터 과학자', '🛰️ AI 연구원', '📊 전략 컨설턴트'],
    'INFP': ['🎨 일러스트레이터', '📚 작가', '🧘‍♀️ 심리상담사'],
    'ENFP': ['🎤 유튜버', '📱 마케팅 기획자', '🎭 공연기획자'],
    'ISTJ': ['📊 회계사', '📂 행정공무원', '🏛️ 사서'],
    'ESFP': ['🎶 뮤지션', '🎬 배우', '🛍️ 쇼핑몰 CEO'],
    'ENTP': ['🚀 스타트업 창업가', '🗣️ 토론가', '📡 기술 컨설턴트'],
    # 나머지도 원하는 만큼 채워넣을 수 있음
}

# 🧩 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요? 🤔", mbti_list)

# 📌 추천 결과 출력
if selected_mbti:
    st.markdown(f"### ✅ {selected_mbti} 유형에게 추천하는 직업은...")
    for job in job_dict.get(selected_mbti, ['직업 정보가 준비되지 않았어요!']):
        st.markdown(f"- {job}")

    st.markdown("✨ 당신의 성향을 살려 멋진 미래를 그려보세요! ✨")

# 📢 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>ⓒ 2025 MBTI Career Recommender. Made with ❤️ in Streamlit.</p>", unsafe_allow_html=True)

