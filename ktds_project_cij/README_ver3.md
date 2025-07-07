개발자 입장에서 직면한 현실
● “이 AI 서비스… 개인정보 유출 안 되나요?”
● “OpenAI API 너무 비싸요”
● “GPT 응답이 이상한데, 왜 그런지 모르겠어요”
● “팀마다 사용량 파악이 안 돼요”
👉 오늘 강의는 이런 실전 문제 해결을 위한 구조화된 가이드를 제공할 예정이랍니다!



Prompt Life-Cycle 5 단계
● 기획 → 작성 → 실행 → 평가 → 버전관리
각 단계별 내용 요약
● 기획 → 해결하려는 문제와 목표를 명확히 정의합니다.
● 작성 → 목표에 맞게 프롬프트 문장을 구성합니다.
● 실행 → 작성한 프롬프트를 모델에 적용해 테스트합니다.
● 평가 → 모델의 응답 품질을 분석하고 개선점을 찾습니다.
● 버전관리 → 프롬프트 변경 이력과 성능을 체계적으로
관리합니다.



기획

- **사전 구축 지식 기반 RAG + 답변 생성**

- 텍스트 요약

작성/실행

3. **문서 기반 RAG 응답 충실도 Factual Consistency, Context Relevance**
**Score 응답이 문서 기반 사실과 일치하는지**



평가표

- **평가항목을 주고 내 mvp 평가해줘 라고 물어보기**



- langflow : langgraph보다 쉽게 사용하고 싶다
  - 빠르게 ai agent 만들 수 있음



**모델 : OpenAI(GPT-4o)**

**데모 : Chainlit / Streamlit 추천**



2가지 기능에 대한 output이 다 포함 된 mvp



- 데이터 안전 : 펄뷰
- 모델 안전 : openai foundry 활용



- 리소스
  - 지역별 로드밸런싱 추천 : 시간대별로 빠른 지역을 알면, 시간대별로 어느 지역 리전을 쓰도록 설정 해둔다던지
  - **지역별 로드밸런싱을 통해서 안정화를 했다**
    - **ex) 10000토큰, 10000토큰 띄워놓고 부하 넘어갔을 때 다른 지역으로 넘어갔다던지 등 안정화 한 부분 보여줘도 좋음**



----

### 개발예시

- 코드 자동 생성기 
  - 원하는 요구사항에 맞춰서 생성하기(ex. 회사 정책에 맞게 코드를 잘 짜달라)
- 코드 리뷰어
  - 주석 없다, 코드 부족하다, 등에 대한 분석 서비스
- 문서 Q&A, RAG 봇
  - 미리 문서를 보유하고 있어야 함.
  - 사내 DB + PDF → 요약·검색
  - Azure AI Search, Llama-Index, Phi-3-mini
- 검색 임베딩 모델 평가기
  - RAG 성능 개선을 위한 임베딩 모델 테스트 데이터셋 생성
  - huggingface E5/labSE, RAG

### 개발 스케쥴

Day 0 (0.5 일) 환경 세팅·데이터/API 열람 ᐟ Azure 리소스·VM, repo 초기화
Day 1 (1 일) 핵심 파이프라인 구현 ᐟ 모델 추론 코드, 핵심 API
Day 2 오전 (0.5 일) 품질 보강 & 테스트 ᐟ 샘플 케이스 20 건 통과
Day 2 오후 (0.5 일) UX 모델 래핑·배포 & 발표자료 ᐟ Streamlit/Gradio 프론트 + PPT

### 질문

https://adorable-hail-415.notion.site/KT-ds-MS-AI-1f9137efedf68028aec6c315379e637e?p=213137efedf680cfbf4bddbe3ce54d6b&pm=s



### 피드백

많은 서비스를 잘 통합해서 인사이트를 뽑아내는 어려운 작업으로 보입니다. 구현시 고려사하에 말씀하신 요소들을 구체화 할 필요가 보입니다.



### 구현

1. 학습 데이터

   1. 고객 요구사항
   2. 관련 파트 내용
      1. 파트
      2. 구현문서(IA명)
      3. 구현내용(IA 문서내용)
         1. MM
         2. 관련 히스토리 IA명

   - [IA 문서 샘플]
     - Part: ReportEngine
       - 기능: 통계 데이터 생성 및 시각화
       - 입력: 날짜, 사용자ID
       - 출력: 차트 데이터

2. 입력 데이터

   1. 고객 요구사항

      ```
      "이런 요구사항에 대해 업무 분배해줘"
      
      너는 SW 설계 분석 전문가야. 아래는 고객의 요구사항이야.
      IA 문서와 연관도 데이터를 참고해서 어느 파트에 영향이 큰지 알려줘.
      ```

3. 출력 데이터

   1. 파트별 연관도(%)
   2. 파트별 구현 예측 내용



++ 기타

- 비슷한 IA문서 검색?



### 시작

- 리소스그룹 : user24-RG-003 / WEST US

- ai foundry 프로젝트 만들기

  - ai.azure에서 새 프로젝트 만들기
  - 모델 배포

- 웹앱 만들기 : 

- ai search : user24-ai-search-003

  ```
  SEARCH_API_KEY=
  SEARCH_ENDPOINT=
  SEARCH_INDEX_NAME=
  ```

- ai service : user24-ai-service-cij-003

  ```
  ```

- open ai : user24-openai-cij-003

  - dev-gpt-4o-cij

  ```
  OPENAI_API_KEY=
  OPENAI_ENDPOINT=https://user24-openai-cij-003.openai.azure.com/
  OPENAI_API_TYPE=azure
  OPENAI_API_VERSION=2024-12-01-preview
  DEPLOYMENT_NAME=dev-gpt-4o-cij
  CHAT_DEPLOYMENT_NAME=dev-gpt-4o-cij
  ```

  





----

### Purview 실습

1. **Microsoft Purview** 계정 만들기
2. 스토리지 계정
   1. 스토리지 브라우저 > blob 컨테이너 > 데이터 업로드
3. 데이터 원본 등록
   1. 데이터 원본 > azure blob storage 추가 
4. scan 검사하기
   1. storage에 purview에 대한 역할 추가 필요
      1. blob reader > 관리ID 추가 
      2. 검사 - 규칙 생성 가능

- 각 자산의 검사는 각 자산(데이터)별로 별개로 동작함



5. Azure AI Foudry 모델 콘텐츠 필터링

   







----

- 추후 고려
  - PTU : 직접 서버를 회사에 할당해서 사용할 수 있게 함
    - 무조건 속도 일정
    - 비쌈 : 24시간동안 계속 돈이 나감(사용여부랑 상관없이)
    - 
