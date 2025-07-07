import streamlit as st
import json
import os
from docx import Document
import zipfile

# JSON 파일 경로
DATA_PATH = "streamlit_data/ia_acs_documents.json"
WORD_DOCS_DIR = "streamlit_data/ia_word_documents_50"

# 데이터 불러오기
def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

data = load_data()

# IA 문서번호 생성기: 현재 문서 수 기준 +1
def get_next_doc_id():
    return f"{len(data) + 1:03d}"

st.set_page_config(page_title="IA 문서 분석 대시보드", layout="wide")
st.sidebar.title("📁 IA 문서 분석 대시보드")

# ⬆️ 기능 2: IA 문서 업로드
st.sidebar.markdown("---")
st.sidebar.subheader("📤 IA 문서 업로드")
uploaded_file = st.sidebar.file_uploader("IA Word 문서를 업로드하세요", type=["docx"])
if uploaded_file is not None:
    new_id = get_next_doc_id()
    save_filename = f"{new_id}_{uploaded_file.name}"
    save_path = os.path.join(WORD_DOCS_DIR, save_filename)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Word 문서 파싱 및 JSON 변환
    docx = Document(save_path)
    paragraphs = [p.text.strip() for p in docx.paragraphs if p.text.strip()]

    parsed = {
        "id": new_id,
        "project_title": paragraphs[1].replace("과제명: ", "") if len(paragraphs) > 1 else "업로드 문서",
        "requirement": next((p for p in paragraphs if p.startswith("요구사항:")), "요구사항: 없음").replace("요구사항:", "").strip(),
        "parts": []
    }

    for i in range(len(paragraphs)):
        if paragraphs[i].startswith("[연관 파트"):
            part = {
                "part_name": paragraphs[i + 1].replace("- 파트 이름: ", ""),
                "role": paragraphs[i + 2].replace("- 구분: ", ""),
                "feature": paragraphs[i + 3].replace("- 기능: ", ""),
                "content": paragraphs[i + 4].replace("- 내용: ", "")
            }
            parsed["parts"].append(part)

    data.append(parsed)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    st.sidebar.success(f"✅ 업로드 및 등록 완료: {save_filename} (ID: {new_id})")

# ⬇️ 전체 Word 문서 압축 다운로드 버튼
st.sidebar.markdown("---")
st.sidebar.subheader("📦 전체 IA 문서 다운로드")
zip_path = "streamlit_data/ia_word_documents_all.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for fname in os.listdir(WORD_DOCS_DIR):
        fpath = os.path.join(WORD_DOCS_DIR, fname)
        zipf.write(fpath, arcname=fname)
with open(zip_path, "rb") as f:
    st.sidebar.download_button(
        label="📁 전체 문서 압축 다운로드",
        data=f,
        file_name="ia_word_documents_all.zip",
        mime="application/zip"
    )

st.title("📊 AI 기반 IA 문서 분석 대시보드")

# 키워드 검색
search_query = st.text_input("🔍 키워드로 IA 문서 검색", "")

# 팀 목록 추출
def extract_teams(data):
    teams = set()
    for doc in data:
        for part in doc.get("parts", []):
            teams.add(part["part_name"])
    return sorted(list(teams))

teams = extract_teams(data)

# UI 상단 선택 필터 영역
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_team = st.selectbox("팀 선택 (연관된 문서 필터링)", ["전체"] + teams)

    def filter_by_team(data, team):
        if team == "전체":
            return data
        return [doc for doc in data if any(p["part_name"] == team for p in doc.get("parts", []))]

    filtered_data = filter_by_team(data, selected_team)

    # 검색 필터 적용
    if search_query:
        filtered_data = [doc for doc in filtered_data if search_query.lower() in doc["project_title"].lower() or search_query.lower() in doc["requirement"].lower()]

    with col2:
        ids = [doc["id"] + ": " + doc["project_title"] for doc in filtered_data]
        selected = st.selectbox("과제 선택", ids) if ids else None
        selected_id = selected.split(":")[0] if selected else None

# 선택된 문서 표시
doc = next((d for d in data if d["id"] == selected_id), None) if selected_id else None

if doc:
    st.subheader(f"📝 과제명: {doc['project_title']}")
    st.markdown(f"**요구사항:** {doc['requirement']}")

    st.divider()
    st.subheader("🔧 연관 파트별 정보")
    for i, part in enumerate(doc["parts"], 1):
        with st.expander(f"파트 {i}: {part['part_name']} ({part['role']})", expanded=True):
            st.markdown(f"- **기능:** {part['feature']}")
            st.markdown(f"- **내용:** {part['content']}")

    matches = [f for f in os.listdir(WORD_DOCS_DIR) if f.startswith(f"{doc['id']}_") or f.endswith(".docx")]
    if matches:
        word_path = os.path.join(WORD_DOCS_DIR, matches[0])
        with open(word_path, "rb") as f:
            st.download_button(
                label="📥 IA Word 문서 다운로드",
                data=f,
                file_name=matches[0],
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.warning("📄 해당 과제의 Word 문서를 찾을 수 없습니다.")
elif search_query:
    st.info("검색된 결과가 없습니다.")
else:
    st.error("문서를 찾을 수 없습니다.")
