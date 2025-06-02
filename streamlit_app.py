import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.title("진주시 CCTV 현황")

# CSV 파일 로딩 (경로 수정 필요)
df = pd.read_csv("./jinju_cctv_20250513.csv", encoding='euc-kr')

# 데이터 확인
st.dataframe(df, height=200)

# 위도/경도 컬럼 이름 일치 여부 확인
df["lat"] = df["위도"]
df["lon"] = df["경도"]

# 지도 생성
m = folium.Map(location=[35.1799817, 128.1076213], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

# 마커 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=row["설치장소"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)

# 지도 출력
folium_static(m)
