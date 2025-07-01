# openai-cij

# 기본 참조 링크
- https://portal.azure.com/
- 

# 1일차
> 교육 url : `https://github.com/KoreaEva/KTds2/tree/main/Day%204`


----

# 2일차
> 교육 url : `https://github.com/KoreaEva/KTds2/tree/main/Day%205`
```
Azure App Service를 사용하여 웹 애플리케이션 호스트
Azure Web App에 Streamlit 배포하기
Storage Account
02. Azure에서 기계 학습 시작
03. Azure에서 자연어 처리 시작
04. Computer Vision 개념 소개
```

### 1. Azure App Service 사용하여 웹앱 배포
- 웹앱 만들기
    - 리소스 그룹 > 내 리소스 그룹 선택 > 웹앱 만들기
    - 인스턴스정보 : 유니크하게 설정 (뒤에 .azurewebsites.net 이 붙음)
    - 코드 : python 3.11 -> 버전이 너무 높으면 안 돌아가는 경우 있음.
    - 지역 : Korea Central
    - 가격 책정 플랜 : B3 (단위 : sku = 각 서비스의 사이즈를 뜻함.)
* token 기반은 사용 안하면 과금되지 않음. But, 웹서버(웹앱)는 만드는 순간부터 과금 됨.
* 환경변수
    - .env 파일에 있는 값들을 여기에 넣으면 호출 시 자동으로 읽어옴.(using os.get_dotenv)
* 스케일 업/아웃
    - 웹서버는 스케일 업보다 스케일 아웃이 더 많고 중요함.
    - 프로덕션용은 sku 선택 후 스케일 자동으로 선택하면 스케일 관리가 자동으로 됨. (인스턴스 10개까지 늘어남)
 
### 2. Azure Web App에 Streamlit 배포하기
- WebAppTest 진행해보기

  
