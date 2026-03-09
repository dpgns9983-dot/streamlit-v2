import streamlit as st

st.set_page_config(
    page_title="스마트 홈 대시보드 - 양하준",
    layout="wide"
)

st.header("스트림릿 배포 테스트중")
st.write("집에 가서 롤 해보기 - 양하준")

st.write("스트림릿 배포 내용 추가합니다")

st.header("오늘 좀 피곤하구려")
st.write()

# 페이지 등록
#st.page("파일경로", title="메뉴이름", icon="아이콘")
# 홈화면
home = st.Page("home.py", title="홈")
# 센서화면
sensors = st.Page("sensors.py", title="센서 현황")
# 전력 화면

power = st.Page("power.py", title="전력현황")

# 메뉴 화면
menu = st.Page("menu.py", title = "메뉴현황")

# 네이게이션 구성
pg = st.navigation({
    "메인" : [home],
    "분석" : [sensors,power],
    "뜬금없이" : [menu]
})

st.sidebar.write("같이 사이드바 형태입니다")
# 선택된 페이지 실행
pg.run()