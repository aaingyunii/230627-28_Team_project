# 필요한 라이브러리 가져오기
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import common

# 한글 폰트 적용
import matplotlib.font_manager as fm

# common 파일을 통해 웹 페이지 탭 꾸미기
common.page_config()

# 한글 폰트 설정
font_path = './NanumGothic.ttf'  # 한글 폰트 파일 경로
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())

# common 파일을 통해 데이터프레임 불러오기
df = common.get_data()

st.title("막대 그래프")

# 시도별 의료기관 수 계산
hospital_count = df['시군명'].value_counts()

st.set_option('deprecation.showPyplotGlobalUse', False)

tab1, tab2 = st.tabs(["Plotly", "Pyplot"])

# plotly로 바차트 만들기
with tab1:
    fig = go.Figure(data=[go.Bar(x=hospital_count.index, y=hospital_count.values)])
    fig.update_layout(
        xaxis=dict(
            title='시도',
            tickangle=90,
        ),
        yaxis=dict(
            title='의료기관 수',
        ),
        title='시도별 의료기관 수',
    )
    st.plotly_chart(fig,
                    use_container_width=True)


# pyplot으로 바차트 만들기
with tab2:
    plt.bar(hospital_count.index, hospital_count.values)
    plt.xlabel('시도', fontproperties=fontprop)  # 한글 폰트 설정
    plt.ylabel('의료기관 수', fontproperties=fontprop)  # 한글 폰트 설정
    plt.title('시도별 의료기관 수', fontproperties=fontprop)  # 한글 폰트 설정
    plt.xticks(rotation=90, fontproperties=fontprop)  # 한글 폰트 설정
    st.pyplot()


