import streamlit as st
import json

# JSON 파일 경로
DATA_PATH = "streamlit_data/ia_acs_documents.json"

# 데이터 불러오기
def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

st.set_page_config(page_title="IA 문서 분석 대시보드", layout="wide")
st.title("📊 AI 기반 IA 문서 분석 대시보드")

# 팀 목록 추출
def extract_teams(data):
    teams = set()
    for doc in data:
        for part in doc.get("parts", []):
            teams.add(part["part_name"])
    return sorted(list(teams))

teams = extract_teams(data)
selected_team = st.sidebar.selectbox("팀 선택 (연관된 문서 필터링)", ["전체"] + teams)

# 팀 선택 필터 적용
def filter_by_team(data, team):
    if team == "전체":
        return data
    return [doc for doc in data if any(p["part_name"] == team for p in doc.get("parts", []))]

filtered_data = filter_by_team(data, selected_team)

# 사이드바 - 과제 선택
ids = [doc["id"] + ": " + doc["project_title"] for doc in filtered_data]
selected = st.sidebar.selectbox("과제 선택", ids)
selected_id = selected.split(":")[0]

# 선택된 문서
doc = next((d for d in data if d["id"] == selected_id), None)

if doc:
    st.subheader(f"📝 과제명: {doc['project_title']}")
    st.markdown(f"**요구사항:** {doc['requirement']}")

    st.divider()
    st.subheader("🔧 연관 파트별 정보")
    for i, part in enumerate(doc["parts"], 1):
        with st.expander(f"파트 {i}: {part['part_name']} ({part['role']})", expanded=True):
            st.markdown(f"- **기능:** {part['feature']}")
            st.markdown(f"- **내용:** {part['content']}")
else:
    st.error("문서를 찾을 수 없습니다.")
