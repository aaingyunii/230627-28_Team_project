import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common

# 한글 폰트 적용
import matplotlib.font_manager as fm

# common 파일을 통해 웹 페이지 탭 꾸미기
common.page_config()


st.title("Scatter Plot")

# 한글 폰트 설정
font_path = './NanumGothic.ttf'  # 한글 폰트 파일 경로.
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())

# common 파일을 통해 데이터프레임 불러오기
df = common.get_data()

# 챗지피한테 물어보기
st.set_option('deprecation.showPyplotGlobalUse', False)

# tab으로 나누기
tab1, tab2 = st.tabs(["Plotly", "Pyplot"])

# plotly로 산점도 그래프 만들기
with tab1:
    fig = go.Figure(data=[go.Scatter(x=df['경도'], y=df['위도'], mode='markers')])
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
    st.plotly_chart(fig, use_container_width=True)


# pyplot으로 산점도 그래프 만들기
with tab2:
    plt.scatter(df['경도'],df['위도'])
    plt.xlabel('경도', fontproperties=fontprop)  # 한글 폰트 설정
    plt.ylabel('위도', fontproperties=fontprop)  # 한글 폰트 설정
    plt.title('소재지 위도와 경도를 이용한 산점도', fontproperties=fontprop)  # 한글 폰트 설정
    plt.xticks(rotation=90, fontproperties=fontprop)  # 한글 폰트 설정
    st.pyplot()





# 소재지 위도와 경도를 사용하여 산점도 그리기
plt.figure(figsize=(10, 6))
plt.scatter(df['경도'], df['위도'])
plt.xlabel('경도')
plt.ylabel('위도')
plt.title('병원 위치 분포')
plt.show()