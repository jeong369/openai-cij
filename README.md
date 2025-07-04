### 참고사항

< 수료기준 >
1인 1agent > 10분 발표

> 자료 : https://adorable-hail-415.notion.site/KT-ds-MS-AI-1f9137efedf68028aec6c315379e637e?p=202137efedf68059adc9c9092561462e&pm=s

> 계정정보
>
> - copilot : emic235455@momail.kr / Tomato723109!
> - ms azure : user24@modulabsbiz.onmicrosoft.com / modu123!
>
> - new ms azure : labuser24@helloaicloud.onmicrosoft.com / !!Seoul2025 > 강사님 개인 tenant.. > 융합대학 실습계정

> 실습 수업자료
> https://github.com/KoreaEva/KTds2 



----

**< 기본 개념 >**
Azure AI Foundry는 마이크로소프트의 Azure 플랫폼 내에서 제공되는 AI 개발 및 배포 도구와 서비스를 포괄하는 개념입니다. 이 플랫폼은 기업과 개발자들이 인공지능(AI) 솔루션을 쉽게 구축하고 배포할 수 있도록 돕기 위해 설계되었습니다.   

주요 기능과 특징은 다음과 같습니다:  

1. **모델 개발**: Azure AI Foundry는 다양한 머신러닝 및 딥러닝 모델을 개발하는 데 필요한 도구와 프레임워크를 제공합니다. 사용자는 Python, R 등 다양한 프로그래밍 언어를 사용할 수 있습니다.  

2. **자동화**: 머신러닝 모델의 훈련, 검증, 배포 과정의 자동화를 지원하여 개발자가 더 빠르고 효율적으로 작업할 수 있게 합니다.  

3. **데이터 준비**: 데이터 전처리 및 탐색을 위한 도구를 제공하여, 모델 훈련에 적합한 데이터를 준비할 수 있도록 돕습니다.  

4. **배포 및 관리**: 모델을 클라우드 환경에 쉽게 배포하고, 운영 중인 모델의 성능을 모니터링할 수 있는 기능을 포함하고 있습니다.  

5. **통합**: Azure의 다른 서비스와 통합되어, 데이터 저장소, 애플리케이션 및 분석 도구와 원활하게 연결할 수 있습니다.  

*Azure AI Foundry는 기업들이 AI 솔루션을 빠르게 개발하고, 이를 비즈니스 가치로 전환할 수 있도록 돕는 강력한 도구입니다. AI 기술을 활용하려는 기업이나 개발자에게 유용한 플랫폼이 될 수 있습니다.*


------
* chatGPT : OPENAI에서 만든 인공지능
* gemini(제미나이) : 구글에서 만든 인공지능 - 대화형



----

### 1일차

**주제 : azure에서 ai를 어떻게 쓰는가**

- 어떤 프로젝트를 만드는게 좋은지 고민..
- 70점 이상이면 pass

1개의 tenant에 묶여있음 -> 작업내용 서로 봄

> ms 교육
- Foundry 모델에서 Azure OpenAI를 사용하여 애플리케이션 개발 -> https://learn.microsoft.com/ko-kr/training/paths/develop-ai-solutions-azure-openai/

1. Azure OpenAI Service 액세스

   - 포털에서 하는 법 << CLI 기반 명령어로 하는 법(관리하기 용이함)
   * 리소스 = 앱에 존재하는 모든 것(데이터베이스 등)
   1-1) 리소스그룹 만들기 : user24-RG > 미국쪽 사용 권장(East US)
   * azure는 클라우드 보안을 통과함(24년 말)
   * 클라우드는 marketplace 랑 동일한 개념. 즉, 쿠팡...?
   1-2) 리소스 만들기
   * Canonical > 우분투 서버 만들기 잘함.
   - Azure OpenAI > (PTUs 사용하면 안됨)
   1-3) 키 및 엔드포인트 설정
   - 키 노출되면 재생성
   1-4) Exlpore Azure AI Foundry portal
   * Foundry > project를 만들면 model catalog(openai service, ai search, 등등)를 전체 다 사용 가능하고, openAI를 만들면 Azure OpenAI만 사용 가능함.


**< 채팅 플레이그라운드 >**
(1) 사용할 모델 언어 정해야 함 : 

- 모델 카탈로그 
  - gpt3.5 : 비싸고 성능 안좋음.
  - gpt 4.5 : 비용 비쌈.
  - gpt-4.1-mini or gpt-4o-mini 중 1개 사용
- 이 모델 사용 > 배포이름으로 구별하기 때문에 "dev-gpt-4o-mini-cij"와 같이 구별해주면 됨(나중에 호출할 때 모델이름이 아니라 배포이름으로 호출하기 때문에 중요함)
- python/openai SDK/key authentication
- 모델 지침 및 컨텍스트 제공 : 너는 동시 통역가야. 이제부터 모든 내용을 영어로 번역해.

(2) code 짜기
- endpoint = 대상 URL의 https://openai-cij.openai.azure.com 까지만
- 응답 : response -> 응답이 2개 이상일 수 있어서 리스트 형식임.

(3) streamlit 실행 명령어 : stremlit run _.py



**< 프로젝트 구상 >** 
=> 수요일까지 구상 필요함....
Azure 기반 생성형 AI 프로젝트 만들기

- 사용자 인터페이스 - 웹버전 - ui 있어야 함 = Streamlit
- 데이터 소스는 선택



----

### 2일차 

**Azure App Service를 사용하여 웹 애플리케이션 호스트(PaaS)**

- Web App / Api App / Logic App

1. **Azure App Service를 사용하여 웹 애플리케이션 호스트 - 웹앱 만들기**

   - 리소스그룹 > 내 리소스 그룹 선택 > 웹앱만들기

   - 인스턴스정보:유니크하게 (.azurewebsites.net)

   - 코드 > python 3.11 - 너무 높으면 안 돌아감

   - 지역 : korea central

   * 각 서비스의 사이즈 = sku (가격 책정 플랜)

     * token 기반 : 사용 안하면 과금 x

     * 웹서버(웹앱) : 만드는 순간부터 과금o

   * 기본 도메인 : cij001.azurewebsites.net 만들어짐.

   * 환경변수 : .env에 있는 값들을 환경 변수에 넣어놓으면 읽을 수 있음

   * 웹서버는 스케일 업보다 스케일 아웃이 더 많음(더 중요함)
     - 프로덕션용 : 인스턴스 10개까지 늘어남
     - 프로덕션용 sku 선택 후 > 자동 선택하면 스케일 관리 자동으로 됨.

2. **Azure Web App에 Streamlit 배포하기 - 배포**
   
   > WebAppTest 해보기
   
   - streamlit run app.py 잘되면 웹앱에 배포해보기
     : https://github.com/KoreaEva/KTds2/blob/main/Day%205/02.streamlit_deployment.md

- Vs Code에 Azure App service 연결

  - extension 설치 : Azure App Service

  - A 라는 모양 누르고 azure 로그인 하면 내 리소스 다 볼 수 있음 (>App Service)

  - pip install streamlit : 웹 서버에는 streamlit이 없을테니까 설치할꺼다

  - azure 포탈
    - 구성 > 시작명령어 : bash /home/site/wwwroot/streamlit.sh

  - 내 리소스 마우스 우클릭 : deploy to web app > 지금꺼 다 지우고 해당 소스 배포하겠다.

+ 추가 설명

  + 배포는 꼬이면 어려움! 잘 해야 함.

    + 웹앱 > 개요 > 다시 시작

    

+ 소스 + Copilot 사용

  + 질의 : Azure Web App 서비스를 만드는데 이름은 cij002 그리고 App Service Plan cij002로 만드는데 sku는 B3로 생성할 예정이고 runtime은 python 3.11 버전으로 코드 방식으로 배포할 수 있는 az 명령을 생성해줘
  + 결과 코드는 copilot 옆에 대시 버튼 눌러서 넣으면 됨 (bash 기반)
	>   - 리소스그룹 : user24-RG
	>   - App service 이름 정하고 ex) cij002



3. **Storage Account - 스토리지 구현**

   * Blob > container(드라이브 역할) : 이걸 제일 많이 씀.
      - 리소스 만들기 : 스토리지 계정 > user24storagecij001(대소문자, 언더바 안먹힘) > Korea central > gen 2 > LIS?

        *- azcopy : 파일 병렬로 올리는거 가능*

        *- 더 나아가 azcopy databox 도 있음*

   * 컨테이너 추가

      * 액세스 변경 : blob으로! 

         ```
         * 비공개 : azure 내에서 접근 가능
         * blob : 선택 불가능 = default 사용안함 > [개요 > Blob 익명 액세스 > Blob 익명 액세스 허용 - 사용]
         * 컨테이너 : 풀 엑세스
           -> 개별 url 만들어짐
           -> 기본 html만 올려두고 이미지만 storage에 놓고 부하를 줄임.
         ```

   

4. **Azure에서 기계 학습 시작 => x**

   

5. **Azure에서 자연어 처리 시작**

  1. PII(개인 식별 정보) 검색 은 개인 건강 정보(PHI)를 포함하여 개인적으로 중요한 정보를 식별합니다.

    - 2~3가지 합쳐져서 개인을 식별할 수 있다고 판단하면 개인정보로 침 / 나중에 풀어줄 수 있음
    - 그 외 사용방법 : 주요정보 제외 한 데이터를 애초에 vectorDB에 넣기
  2. 핵심 구 추출 은 구조화되지 않은 텍스트의 주요 개념을 나열합니다.

  ```
  1) 개인정보 포함여부, 로그에서 주요 단어(어떤걸 보고 고쳐야 하는지 볼 수 있나?)
  => *** VOC 문의/답변 -> 분류 -> 대처방안 요약?
   - Extract PII : 개인정보 추출해서 **로 변경
   - Extract key phrases 긍정/부정 분류 or 키워드 분류 
   - 요약
  ```



- 리소스 만들기

  -  `언어 서비스` 검색 > 만들기 ( 옵션 : 사용자 지정 질문 답변 -> pdf 등 우리가 업로드 한 파일의 내용으로 답변 생성 (단, 월 15000원? 고정비용 발생) )

  - 지역 선택

    - 잘못 선택하면 특정 기능이 안되는 지역이 있음 -> https://www.perplexity.ai/ > `Azure langauge service에서 language understading 지원 되는 지역을 알려줘` > 2개 다 체크된 지역으로 만들면 됨) > East US/이름/S

    * 지역은 중국, 독일껀 약관이 다르기 때문에 안 쓰는게 좋음


- 생성은 azure portal에서 만들기

- 사용은 개요 > language studio 시작하기 > sign in
  
   - 접근 가능한 endpoint 입력하면 python으로도 사용 가능
   
   

* language understanding

   > 챗봇 만들 때 필요

   1. 정의 : 
      - Intent : 인사greeting/주문order/배달delivery
        - 나중에 intent 미감지 된 애들이 모이는데 이거 따로 학습 시켜주면 됨
   2. Data labeling : 각 intent별로 발화 입력하고 save changes
      - entity 감지해야 답변이 나옴
      - 라벨링 할 때, 발화에서 각 단어에 intent를 만들어서 넣어줄 수 있음. (수량의 경우, 한국어는 max 수량까지 다 넣어줘야 인식이 가능함.. 영어는 one만 입력해도 다 가능한데)
      - 여러개 entity 있을 때 순서도 중요함.
   3. Training jobs > 모델 만들기
   4. Deploying a model > endpoint 만들기 > get prediction url : request 코드 있음
   5. Testing deployment : 테스트 가능



*- azure for students : 학교 계정 > 1년 100달러 무료*



6. **Computer Vision 개념 소개**

```
- computer vision => 얼굴 있다 없다만 판단
  - computer vision : 이미 학습된 버전
  - custom vision : 우리 사진을 학습시켜서 사용 가능한 버전
- face api 해야 얼굴 인식
```

- Computer Vision 사용하기
  - 리소스 만들기 > Computer Vision - Microsoft | Azure Service
  - 지역 : 거의 모든 지역에서 다 서비스 가능함.
- 서비스 사용하기 : vision studio



----

### 3일차

> 1기 프로젝트 참고 : https://github.com/KoreaEva/KTds/tree/main/MVP
- 데이터 수집 : 더미 데이터로만 돌아도 된다
- 가이드(매뉴얼) 자동 생성 에이전트 : 문서 작성 agent
- 수요 예측 및 추천 모델 : Azure에서 사용하는 머신 러닝이 있다
- 자연어 기반 sql 쿼리 생성 및 성능 최적화 도우미



0. **리소스 만들기**

* 소스 + copliot 이용

  > east us 지역에 user24-RG라는 이름으로 리소스 그룹을 만들 수 있게 스크립트를 작성해줘
  > `az group create --name user24-RG --location eastus`

  >  user24-RG 리소스 그룹에 computer vision 서비스를 서비스 이름은 user-computervision-cij001이고, sku는 free가 아닌걸로 eastus 지역에 생성하는 스크립트를 작성해줘
  > `az cognitiveservices account create --name user24-computervision-cij001 --resource-group user24-RG --kind ComputerVision --sku S1 --location eastus`



1. **Computer Vision 실습 이어서 진행**
   1. 이미지 분석
   
      - `ENDPOINT_URL = ENDPOINT + "vision/v3.2/analyze"`
   
      - 결과 : `result['description']['captions'][0]['text']`
   
   2. 객체 감지
   
      - `ENDPOINT_URL = ENDPOINT + "vision/v3.2/detect"`
   
      - 결과 : `result['objects'][0]` > `'rectangle': {'x': 75, 'y': 33, 'w': 184, 'h': 141}`
   
      - 좌표로 나오는 결과를 원래 이미지 위에 bounding box로 표시하는 함수 필요 : `from PIL import Image, ImageDraw, ImageFont`
   
   3. OCR
   
      - `ENDPOINT_URL = ENDPOINT + "vision/v3.2/ocr"`
   
      - 결과 : 각 문단, 문장, 단어별 좌표가 나옴.
        - 문단 - region
        - 문장 - line
        - 단어 - word



*Azure AI Document Intelligence*

- 양식이 정해져 있는 문서의 경우, 1개의 문서에 대해서 5개 이상의 샘플 데이터를 학습 시키면 문서 만들어 줌.
  - ex) 타이틀, 작성자, 내용 등등 항목을 쌍(키-값)으로 인식
  - **ex) 명세서 항목별로 학습 시켜서 분석 가능.**



2. **Azure ML 실습**

   > https://portal.azure.com/

   1. 새로운 계정으로 로그인 > 리소스 만들기

      `labuser24@helloaicloud.onmicrosoft.com` > `user24-RG`

   2. **Azure Machine Learning 만들기** 

      - 이름 : `user24-ml-000001` 
      - 지역 : `East US 2`(지역 아무거나)

      - 스토리지 계정 : 데이터 찾을 때 이름 맞춰서 지어놔야 나중에 찾기 편함.
      - 키 자격 증명 모음 : ML에서 이건 기본
        - 서비스 여러개 사용할 때 key valt 활용하면 보안성에서 좋음 <- 서비스 사용 시, 여기에다 허락 맡고 들어옴.
      - Application Insights : ML에서 이건 기본
      - 컨테이너 레지스트리(ACR)

   3. Machine Learning 개념

      - workspace
        - compute
        - data
        - model
        - 배포하면, endpoint
      - python으로 관리

   4. 실행 : Launch Studio

      1) 컴퓨팅 자원 만들기

         - 컴퓨팅 > 컴퓨팅 인스턴스(가상머신): `labuser24-vm`
           - 크기 : D - 범용 목적 / F - 컴퓨팅 목적

      2) 작성

         1) Notebooks : 여기 작성된 python으로 아래 "자산"에 있는 요소들을 컨트롤 할 수 있음

         2) 자동화된 ML : AutoML

            > 실시간으로 바뀌는 데이터의 경우, 유용함

            - 새로운 자동화된 ML 작업 생성
              - 작업 형식 선택 : 분류/회귀/시계열 예측/자연어처리
              - 데이터 자산 만들기
                - 표 형식 > titanic.csv 데이터 넣기
                - 자산 원본 > Azure Storage - SQL DB 순으로 많이 씀
                - 저장소 : Blob Storage(아까 위에서 만든 스토리지)
                - 스키마 설정 - 불필요한 데이터 삭제, 유형 설정 등
              - 작업 설정
                - 대상 열 : y(label) 지정
                - 추가 구성 설정 : accuracy
                - 유효성 검사 유형 : 데이터 없으면 - k 교차 / 일반적으로는 "자동"
              - 컴퓨팅
                - 유형 : 인스턴스
                - 인스턴스는 1시간동안 미사용이면 꺼지기 때문에 재시작 후 사용하면 됨.

            > 실행되면, 자산 > 작업(Job)에서 확인 가능
            >
            > 학습이 완료되면, 상단 "모델 + 자식 작업"에서 확인 가능
            >
            > - 각 알고리즘별 정확도 확인 가능 / 가장 높은 알고리즘이 상단으로 올라감.
            > - 클릭해서, 매트릭을 보면 각 결과값을 볼 수 있음

         3) 디자이너

            > tool / canvas / pipeline 으로 구성되어 있음.

            1. 데이터셋 설정

            2. 데이터셋 나누기 

               - split data -> 데이터를 train/test로 나누기 위함.

               - Fraction of rows : 0.8 (첫번째 데이터를 80%로 설정하겠다)

            3. 알고리즘 설정

               - Two-Class Decision Forest

            4. 학습 모델 설정

               - Train Model
               - 알고리즘 : 3번
               - 데이터셋 : 2번의 train(80%) 데이터 연결

            5. 모델 점수 확인

               - Score Model
               - 모델 : 4번
               - 데이터셋 : 2번의 test(20%) 데이터 연결

            6. 평가 모델

               - Evaluate Model
               - 데이터셋 : 5번

            7. 실행

               - 구성 및 전송
               - 새로 만들기 > `exp_titanic_user24_design`

            > 실행되면, 자산 > 작업(Job)에서 확인 가능
            >
            > 실시간 작업 현황을 볼 수 있음 > "데이터 미리보기"에서 결과 확인 가능

      3) 배포

         > 작업(Job) > 게시 > endpoint 배포

         - 새로 만들기 > `endpoint_exp_titanic_user24_design`

         > 실행하면, 자산 > 파이프라인 에서 확인 가능
         >
         > - 이용 가능한 REST endpoint 발급 후 사용 가능함.

      4) 자산

         - 모델
           - 위에서 구성한 모델을 쓰려면 직접 등록해야 한다
         - 엔드포인트

   

3. **Azure AI Search 실습**

   > Azure AI 검색은 광범위한 데이터 원본을 인덱싱 및 쿼리할 수 있고 스케일링 성능이 뛰어난 종합 검색 솔루션을 만들 수 있는 클라우드 기반 솔루션을 제공합니다.

   1. 개념

      1. 인덱스

         - 타입

           - 텍스트 타입 : just serach

           - 벡터 타입 : 임베딩 필요
             - 인덱싱 차원 = 검색 차원 일치 시켜야 함.

         - 실제로 저장되는 위치 : 복제본

           > 속도 향상을 위해선

           	1) 복제본(검색노드) 수 증가시키기
           	2) 파티션(복제본을 나누는/디스크의 수) 수 증가시키기

         - 검색 단위 수는 복제본 수와 파티션 수를 곱한 값(RxP=SU)

         - 인덱싱 주기 설정 가능 : 문서 내용이 계속 바뀌는지, 안바뀌는지 등에 따라 다름

      2. 데이터 원본 지원

         - Azure Blob 스토리지 컨테이너의 비구조적 파일
         - Azure SQL Database의 테이블
         - Cosmos DB의 문서

      3. skillset - Azure AI Service 활용 - 원본 데이터 보강 파이프라인 정의

         - named entity
         - 긍정/부정 분류
         - 내가 만든 모델을 활용하여 결과를 붙여서 사용도 가능

         -> 인덱서(전체 인덱싱 프로세스를 구동하는 엔진)를 통해 실행 가능

         - 이벤트 감지해서 실행 가능 = Azure Functions

         -> 인덱스(인덱서가 돌아서 나온 인덱싱 프로세스의 결과) : json 결과

      4. 연습

         `https://labclient.labondemand.com/LabClient/b7fe56cc-4e44-4838-80ce-dd2d138d7924`

         

----

### 4일차

> **lab_01.md 내용**

1. 리소스그룹 만들기

   - 지역 : West US

2. AI Serach 생성

   - `user24-ai-search-cij-001`
   - 지역 : 리소스 그룹이랑 동일하게
   - 가격 책정 계층 : 기본

3. AI Service 생성

   - `user24-ai-service-cij-001`
   - 지역 : 리소스 그룹이랑 동일하게
   - 가격 책정 계층 : Standard

4. 스토리지 계정 생성

   - `user24storagecij001`
   - LRS

   > 들어가기

   - blob > container 추가 > `pdf-data` > reviews 업로드

5. open ai 생성

   - `user24-openai-cij-001`
   - 지역 : 리소스 그룹이랑 동일하게 / ai-search하고 같은 지역
   - 가격 책정 계층 : Standard
   - 사용 : AI Foundry portal

> 데이터 연결

1. 데이터 가져오기 전, openai에서 모델을 리소스에 배포해야 함
   - ai search > 모델 카탈로그 > embedding 모델(text-embedding-3-small / 표준)
   - ai search > 모델 카탈로그 > 언어 모델(gpt-4.1-mini / 글로벌 표준)
2. search ai > 데이터 가져오기 및 벡터화 > blob stoarage > RAG
   - 데이터에 연결 : 4번 storage 연결 > blob > container > 업로드 한 데이터
   - 텍스트 벡터화 : 5번 openai 연결 > embedding model
   - 이미지 벡터화 및 보강 : pdf 파일 내에 이미지가 있고 이미지 안의 text도 필요할 때 사용.
   - 고급 설정 
     - 의미 순위매기기 : 시맨틱 리랭킹
     - 인덱싱 예약 : 데이터 업로드 주기에 따라 인덱싱 주기 설정

> index-review 만들기 성공 : 검색 탐색기를 사용하에 데이터 검색 시작
>
> - search > 검색 관리 > 인덱서 에서 확인 가능

- 검색 탐색기 > 인덱스 > text 조회 가능

> 실제 활용

1. openai > 채팅 플레이그라운드 > 데이터추가 - 데이터 원본 추가
   - 데이터 원본
     - 원본을 어떤걸 선택해도 결국 AI Search를 사용하게 되어있음
     - AI 검색 서비스 - AI search
     - AI 검색 인덱스 - index-review
     - 우리가 만든 인덱스가 벡터 기반이니, 벡터 검색 추가 - embedding model 선택
   - 데이터 관리
     - 하이브리드(벡터+키워드)
       - quert > text search + vector search -> merge -> rerank
   - 데이터 연결 - api 키

2. 채팅 test
   - 채팅 그라운드에서는 언어모델이 붙었을 때를 가정하고 test 하는 환경
   - 실제 우리가 사용할 떈, search 서비스에 gpt모델을 붙여서 사용해야 함



> **lab_02_AzureCLI.md 내용**

- .env

    ```
    OPENAI_API_KEY=
    OPENAI_ENDPOINT=https://user24-openai-cij-001.openai.azure.com ## foundry portal에서 배포 > endpoint의 .com 까지만 사용
    CHAT_DEPLOYMENT_NAME=dev-gpt-4.1-mini # 배포 > 배포정보-이름
    EMBEDDING_DEPLOYMENT_NAME=dev-text-embedding-3-small
    
    SEARCH_API_KEY= # 관리자키:생성 (쿼리 키:조회만 가능)
    SEARCH_ENDPOINT=https://user24-ai-search-cij-001.search.windows.net ## 개요 > URL
    SEARCH_INDEX_NAME=index-review
    ```
    
- rag-app.py : 가장 기본적인 구조만



>  실습파일 활용
>
> https://github.com/MicrosoftLearning/mslearn-knowledge-mining

1. 01-azure_search

   - `UploadDocs.cmd` : 윈도우에서 실행시키기 위한 배치 파일

   ```cmd
   @echo off
   SETLOCAL ENABLEDELAYEDEXPANSION
   
   rem Set values for your storage account
   set subscription_id=YOUR_SUBSCRIPTION_ID #개요 > 구독 ID
   set azure_storage_account=YOUR_AZURE_STORAGE_ACCOUNT_NAME #storage name
   set azure_storage_key=YOUR_AZURE_STORAGE_KEY #보안네트워킹 > 액세스키
   
   # 컨테이너 만들고
   echo Creating container...
   call az storage container create --account-name !azure_storage_account! --subscription !subscription_id! --name margies --auth-mode key --account-key !azure_storage_key! --output none
   
   # 파일 업로드
   echo Uploading files...
   call az storage blob upload-batch -d margies -s data --account-name !azure_storage_account! --auth-mode key --account-key !azure_storage_key!  --output none
   ```



- Azure CLI 설치

  - [MSI(Microsoft Installer) 사용하여](https://learn.microsoft.com/ko-kr/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=msi) Windows에 설치 > cmd에서 `az version`으로 설치 확인

  

2. UploadDocs.cmd 실행하면 자동으로 생성됨.



> **lab_03.md**

- 데이터 가져오기(일반 텍스트)
   - 데이터 소스 : Blob
   - 원본 이름 : margies-data
   - 추출 : 콘텐츠 및 메타데이터
   - 연결 문자열 : storage > 액세스키 > 연결 문자열
   - 컨테이너 이름 : margies

   > 원본 스키마 적용

   - 인식 기술 추가 > 보강추가
     - 보강 세분성 수준 : 원본 필드 <- 2~3장 짜리면?
     - 보강 필드는 나중에 변경하기 어려움.
     - 인덱스 필드
       - 조회가능에 체크를 해야 검색 가능

   > 생성완료 -> 일반이기 때문에 벡터 인덱스 할당량 사용량=0

   

> **lab_04.md & lab_05.md** 

- 인덱스 조회

   ```sql
   {
     "search": "New York",
     "count": true,
     "select": "metadata_storage_name,keyphrases",
     "filter": "metadata_author eq 'Reviewer'"
   }
   ```

   - select : output 컬럼 설정
   - filter : 조건 설정

- JSON으로 정의 한 내용을 AI Service REST 인터페이스를 활용하여 생성, 수정

  - `modify-search.cmd`
  - ai_service 를 통해 skillset 설정
    - `skillset.json`
    - `index.json`
    - `indexer.json`

  > 실행하면 index 수정 됨.

- 수정 된 인덱스 조회

  ```sql
  {
    "search": "London",
    "select": "url,sentiment,keyphrases",
    "filter": "metadata_author eq 'Reviewer' and sentiment eq 'positive'"
  }
  ```

  

> **lab_06.md** 

- 검색 클라이언트 생성
  - `margies-travel/app.py`
  - ai search 활용
    - `pip install flask`
  - pdf파일이 안 열리면, 컨테이너margies의 액세스 수준을 변경해주면 됨. (액세스 수준 변경 > blob)



----

### 5일차

> MVP에선 이 부분은 사용 안하는게 좋음. (LLM이 아니라 RAG까지만)
>
> LLM은 학습 오래 걸리고, 데이터 500건 ~ 1000건 이상이어야 효과 좋음. 
>
> 파인튜닝은 데이터 만드는 실습이다



> **Azure AI Foundry를 사용하여 언어 모델 미세 조정**

- 기존 : openai > ai foundry : openai만 사용 가능
- 지금 : ai foundry > 프로젝트 만들기 : openai, 기타 등등 다 사용 가능

1. 모델 사용 > 프로젝트 만들기 `user24-project` / 지역은 지정된 장소만(`Sweden Central`)



> **Azure에서 AI 에이전트 개발 시작**

- AI 에이전트를 만들꺼면 lagnGraph를 활용하는게 더 낫다.
- 8월에 업데이트 후에 사용하는게 좋을지도

- 그럼 어느게 우선? merge? 기존 데이터 아니면 search?
- 지식 추가 > 파일 > 업로드 후 > 새 벡터 저장소 만들기
  - agent가 이 지식대로 대답하는지 확인

- 쉽게 만들 수 있지만 확장성 떨어짐



> **Azure AI Foundry 에이전트 서비스를 사용하여 AI 에이전트 개발**



> **Azure AI 음성 서비스를 사용하여 음성 번역**









----

# MVP 기획

2. **고객 요구사항 분석 서비스**

   > ia 문서 : 고객 요구사항, 관련 업무, 개발 내용 등이 담긴 문서

   - 기획 의도
     1. AS-IS
        - 각 파트별로 각자 개발 완료 후 모여서 개발 리뷰 및 연관도 파악으로 수정사항 빈도수 높음.
        - 개발 공수 높음 
     2. TO-BE
        - 연관 파트 쉽게 파악 가능
        - 업무 개발 전에 영향도 파악 쉬움
        - 업무 개발/운영 영향도 분석 후 분배 가능으로 개발공수 적어질 가능성 높음
   - 개발 단계
     - 고객 요구사항 있음
     - 각 파트별 업무 연관 관계 데이터 있음
     - 각 파트별 ia 문서 있음
       - ia문서는 파트별 동일한 규격으로 5개 이상 샘플 필요
     - 개발 된 결과 필요
   - 관련 기능
   
   

### **< GPT 기반 최종 정리 >**

## ✅ AI 기반 업무 영향도 분석 및 최적화 지원 도구



## 📌 1. 개요 및 목적
고객의 요구사항과 각 파트의 IA 문서를 기반으로 업무 간 연관도 및 영향도를 자동 분석하여 개발/운영 업무를 최적화하는 AI 기반 분석 지원 도구입니다.
( ※ IA 문서 : 고객에게 공유되는 최종 개발 산출물 )

- 요구사항에 대해 **관련 파트와 영향도 자동 도출**

- 개발/운영 전 **연관도 분석**을 통해 업무 누락 및 중복 방지

- 빠른 영향도 분석을 통한 개발/운영 공수 예측 및 **업무 분배 지원**

- 장애 발생 시 영향 범위 자동 추정 및 대응력 향상

  

## 🔧 2. 활용 기술 및 Azure 서비스

| 기능                             | 사용 서비스                               |
| -------------------------------- | ----------------------------------------- |
| 문서 이해/요약                   | Azure OpenAI + Prompt Engineering         |
| 파트별 연관도 분석               | Azure Cognitive Search + Custom Embedding |
| 고객 요구사항 분석 → 영향도 추론 | Azure OpenAI (GPT)                        |
| IA 문서/결과 데이터 저장         | Azure Blob Storage 또는 Cosmos DB         |
| 서비스 실행                      | Azure Function 또는 Logic App             |
| API 통합                         | Azure API Management                      |



## ✅ 3. 구현 단계별 아키텍처 설계

#### 🟦 [1단계] 데이터 수집 및 전처리

- 📂 데이터:
  - 고객 요구사항 텍스트
  - IA 문서 (파트별로 정형화된 포맷 필요)
  - 파트 연관도 데이터 (예: 모듈 간 의존도 매트릭스)
  - 개발 결과 요약본 (optional)
- 📌 전처리 예시:
  - IA 문서에서 "기능명, 입력/출력, 의존 모듈" 추출
  - 고객 요구사항을 문장 단위로 분할

> 샘플 데이터 준비 필요

- 파트

| 파트   | 업무                    | 담당자                         |
| ------ | ----------------------- | ------------------------------ |
| Part A | 고객 정보 관리          | 김사원, 박부장                 |
| Part B | 사용자 인증 관리        | 조대리, 양팀장                 |
| Part C | 온라인 결제 시스템 관리 | 이차장, 서과장, 류대리, 임사원 |
| Part D | 장애 대응               | 안부장, 전대리, 민사원         |

- 담당자 분담표

**개발 역할**은 기능 설계, 코드 구현, 시스템 연동 등을 담당

**운영 역할**은 정책 수립, 품질관리, 모니터링, 장애대응 등을 담당

한 파트 내에서도 개발/운영 역할이 명확히 분리되어 있음

| 파트   | 주요 업무               | 담당자 | 역할 분류 | 세부 역할 및 비고                       |
| ------ | ----------------------- | ------ | --------- | --------------------------------------- |
| Part A | 고객 정보 관리          | 김사원 | 개발      | 고객정보 등록/수정 기능 구현            |
|        |                         | 박부장 | 운영      | 고객 데이터 품질 관리 및 정책 검토      |
| Part B | 사용자 인증 관리        | 조대리 | 개발      | 로그인, OTP, 계정잠금 로직 개발         |
|        |                         | 양팀장 | 운영      | 인증 정책 수립 및 보안 시스템 운영 총괄 |
| Part C | 온라인 결제 시스템 관리 | 이차장 | 개발      | 결제 처리 로직 및 정산 기능 구현        |
|        |                         | 서과장 | 운영      | 결제 정책 수립 및 거래 흐름 모니터링    |
|        |                         | 류대리 | 개발      | 외부 결제 연동 API 구현 (카카오페이 등) |
|        |                         | 임사원 | 운영      | 결제 화면 UI 테스트 및 배포 후 점검     |
| Part D | 장애 대응               | 안부장 | 운영      | 장애 대응 매뉴얼 수립 및 정책 책임      |
|        |                         | 전대리 | 개발      | 장애 감지 로직 및 알림 시스템 구현      |
|        |                         | 민사원 | 운영      | 장애 로그 분석, 운영 보고 자동화        |

- 고객 요구사항
  - 샘플 50개 파일로 저장

| 요구사항 ID | 제목                           | 영향 받는 파트     | 영향 설명                                           |
| ----------- | ------------------------------ | ------------------ | --------------------------------------------------- |
| REQ-001     | 로그인 기능에 OTP 추가         | **Part A, Part D** | 인증 로직(Part A), OTP 입력 UI(Part D)              |
| REQ-002     | A 파트와 B 파트 간 실시간 연동 | **Part A, Part B** | A 파트에서 입력한 데이터를 B 파트 화면에 표시       |
| REQ-003     | 고객정보 변경 이력 관리 기능   | **Part B, Part D** | 이력 저장 로직(Part B), 이력 조회 탭 UI(Part D)     |
| REQ-004     | 결재라인 설정 기능 확장        | **Part C, Part D** | 결재 단계 확장(Part C), 동적 UI 적용(Part D)        |
| REQ-005     | 시스템 장애 시 자동 알림       | **Part C, Part D** | 장애 감지/알림 로직(Part C), 팝업/토스트 UI(Part D) |



------

#### 🟦 [2단계] IA 문서 검색 및 벡터화

- **Azure Cognitive Search + Custom Embedding (Azure OpenAI Embedding 모델 사용)**
   → IA 문서/고객 요구사항을 벡터화하여 유사도 기반 검색 가능

- 예시:

  ```
  python복사편집# 문서 임베딩 예시
  embedding = openai.Embedding.create(input="고객 요구사항 텍스트", model="text-embedding-ada-002")
  ```

------

#### 🟦 [3단계] 요구사항 분석 및 영향도 예측 (프롬프트 설계)

- GPT 프롬프트 예시:

  ```
  markdown복사편집[시스템 메시지]
  너는 SW 설계 분석 전문가야. 아래는 고객의 요구사항이야.
  IA 문서와 연관도 데이터를 참고해서 어느 파트에 영향이 큰지 알려줘.
  
  [요구사항]
  - 고객이 로그인 후 대시보드에서 통계 리포트를 조회할 수 있어야 함.
  
  [파트 연관도 정보]
  - Auth → Dashboard → ReportEngine
  
  [IA 문서 샘플]
  - Part: ReportEngine
    - 기능: 통계 데이터 생성 및 시각화
    - 입력: 날짜, 사용자ID
    - 출력: 차트 데이터
  ```

  → GPT가 **영향 파트 순위**, **변경 필요 포인트**, **추가 고려사항** 등을 정리해줌.

------

#### 🟦 [4단계] 자동화 파이프라인 구성

| 구성 요소          | 설명                                   |
| ------------------ | -------------------------------------- |
| 🧠 GPT API 호출     | 프롬프트 기반 영향도 분석 수행         |
| 🔍 Cognitive Search | 유사 IA 문서, 유사 요구사항 검색       |
| ⚙️ Azure Function   | 신규 요구사항 등록 시 자동 실행        |
| 🗂️ 결과 저장        | 분석 결과, 추천 파트, 연관도 기록 저장 |



------

#### 🟦 [5단계] 최종 결과 예시

> 고객 요구사항: "대시보드에서 기간별 통계 확인 기능 추가"

- 예상 영향 파트: `Dashboard`, `ReportEngine`
- IA 문서 참고: ReportEngine v1.3, Dashboard v2.1
- 예상 개발 공수: 3MD
- 참고 사례: 유사 요구사항 #024, #047
- 추천 담당자: A파트 김XX, B파트 박XX



## 4. 🎯 기대 효과
- 공수 절감 : 영향도 높은 파트를 선제적으로 분석하여 수정 빈도 감소
- 협업 향상 : 파트 간 의존성을 시각적으로 공유 가능
- 품질 향상 : 누락 없는 업무 설계 및 리뷰로 결과물 품질 안정화
- 운영 효율성 향상 : 서비스 이슈 발생 시 영향 받는 파트 자동 식별 및 관련 문서 추천 가능



## ⚠️ 5. 구현 시 고려사항

| 항목                 | 고려내용                                                     |
| -------------------- | ------------------------------------------------------------ |
| 📄 데이터 품질        | IA 문서와 연관도 데이터의 **표준화 및 정합성** 확보 필요     |
| 📁 문서 포맷          | IA 문서와 고객 요구사항은 **구조화된 템플릿**이 바람직 (ex. JSON, YAML) |
| 🧠 AI 프롬프트 설계   | GPT가 오판하지 않도록 **명확하고 일관된 프롬프트 규칙** 설정 |
| 🔍 유사도 검색 정확도 | IA 문서 간 유사도 계산 시 **Embedding + 검색 파이프라인 정밀도 조정 필요** |
| 📊 결과 해석 UI       | 분석 결과를 이해하기 쉽게 **비개발자용 시각화(플로우 차트 등)** 제공 고려 |
| 🔐 보안 및 접근 제어  | IA 문서에 민감한 정보가 있을 경우 **접근 권한/보안정책 필요** |



## ✅ 6. 다음 단계 (추천 순서)

1. **IA 문서 샘플 최소 5개 확보**
2. 각 문서 구조를 분석하여 **프롬프트 설계** → 나와 함께 다듬기 가능
3. Azure OpenAI 리소스 준비 (Chat + Embedding 모델)
4. Cognitive Search 설정 (원한다면 샘플 코드 제공 가능)
5. Azure Function으로 자동화 → 고객 요구 등록 → 분석 → 알림



## ✅ 7. 추가로 도와드릴 수 있는 것

- 프롬프트 설계 템플릿
- IA 문서 요약 자동화 스크립트
- 벡터 검색 예제 (Cognitive Search)
- Azure Function 템플릿
- IA 구조 정의 가이드




### **< 발표 준비 >**

1. 개발 목적

|       | 설명                                                         |
| ----- | ------------------------------------------------------------ |
| AS-IS | 각 파트 별로 요구사항 받아서 개발 -> 개발팀에서 연관 파트끼리 알아서 연락해서 개발 진행 -> 모든 파트 개발/운영진 모여서 연관도 파악 및 공유 -> 운영팀 테스트 시 관련 파트 알 수 없음(개발팀에서 공유해주지 않으면 본인 파트 부분만 테스트 진행) -> 파트별 교차 부분 장애 grey 영역 발생 |
| TO-BE | INPUT으로 과제번호, 과제명, 관련 키워드 넣으면, 1) 고객 요구사항 2) 연관 파트 3) 영향도 4) 히스토리 등을 OUTPUT으로 도출해서 운영 업무 효율화 UP / 장애 대응 |

2. 추후 개발 사항
   - IA 문서와 연관도 데이터의 **표준화 및 정합성** **확보 필요**
   - IA 문서와 고객 요구사항에 대한 **구조화된 템플릿 필요**
   - IA 문서에 민감한 정보가 있을 경우 **접근 권한/보안정책     필요**
3. ※









----

**< 기타 아이디어 >**

> - 기존 데이터를 Azure AI Search에서 인덱싱하고 결과 가져오기 가능
> - langchain으로 개발하고 langgraph로 복잡한 워크플로우를 구성한 후, langsmith나 langfuse로 모니터링 및 최적화



1. **외부채널 BCC 서비스 호출 추이 분석** 고도화

   - 기획 의도

     1. AS-IS : 통합검증플랫폼 기반) 건수 증가율에 따라 10% 이상인 경우 이상징후라고 탐지하고 수동으로 모니터링 진행 중 

     1. TO-BE : 실시간 데이터 추이 분석 및 이상징후 탐지
        - 기간별 호출 건수를 학습
        - 현재 호출된 건수가 이상징후인지 예측

   - 개발 단계
     - 채널별 호출 데이터 필요
       - 일자 / 채널 / bcc 서비스 / 건수
   - 관련 기능

   

3. 비몬 모니터링 탐지 서비스 고도화

   

4. 배포 변경사항 트래킹 : 자연어로 하는 시스템 질의

   ```
   사용 서비스: Azure OpenAI + Azure App Service
   “지난주에 배포된 버전의 주요 변경 사항은?”
   
   “dev 서버의 CPU 사용률이 최근에 급등했나?”
   
   → 이런 질문을 자연어로 던지면 내부 데이터 기반으로 답변하는 AI 운영 도우미 챗봇 구축
   ```

   > 자연어로 서버 상태나 배포 기록 등을 물으면 AI가 답변해주는 시스템 운영 도우미

   ### 🎯 **사용 목적**

   - 운영자/개발자가 **"지금 서버 상태 어때?"** 같은 질문을 할 수 있고
   - GPT가 로그/메트릭/배포 기록 등을 분석해 자연어로 **요약/설명**

   ### 🧩 **사용 구성요소**

   | 구성                                     | 설명                                |
   | ---------------------------------------- | ----------------------------------- |
   | **Azure OpenAI Service**                 | GPT-4 기반으로 자연어 처리          |
   | **Azure Monitor / Application Insights** | 메트릭, 로그, 트레이스 수집         |
   | **Azure Functions / Logic Apps**         | API 연결 또는 데이터 가공 로직 처리 |
   | **Azure App Service or Bot Service**     | 챗봇 형태로 사용자 질의 처리        |
   | (선택) Azure Cognitive Search            | 시스템 문서 검색 연동 가능          |

   ### **주의사항**

   - **정확한 KQL 쿼리 구성**은 GPT의 Prompt 설계에 달려 있음

   - 민감한 데이터 접근 시 GPT에 직접 넘기지 않고, **Azure Functions를 통해 필터링** 필요

   - GPT에게는 “질문 → 내부 쿼리 변환” 역할만 맡기는 게 안정적

     

5. AI 기반 테스트 자동 생성

   ```
   사용 서비스: Azure OpenAI + Azure DevOps
   단위 테스트 코드 자동 생성 (예: Java, Python, JavaScript)
   
   기존 코드의 로직 흐름을 이해하고 커버리지를 높이기 위한 테스트 시나리오 제안
   ```

   - ia 문서 집어넣으면, 관련 화면 / 코드 > 영향도 파악 가능? 
   - 코드 수정 시 영향도 파악
   - 테스트 케이스 제안



6. 장애 발생 시, 담당자한테 자동 알림 서비스

-> 이미 있네 

**오류 로그 기반으로 최근 장애를 분석하고, 담당자에게 자동 알림을 보내는 서비스**는 운영 효율을 크게 높여줍니다.
 Azure 서비스로 이를 구축하는 흐름을 **실제 아키텍처 + 구현 단계**로 정리해드릴게요.

------

## ✅ 목표

- **최근 오류 발생 → 분석 → 담당자에게 자동 알림**
- GPT가 **원인 요약 + 해결 힌트**까지 포함한 메시지 생성 가능

------

## 🔧 아키텍처 구성도

```
mathematica복사편집(1) 로그 수집
Azure Monitor / Application Insights
        ↓
(2) 트리거
Log Alert Rule or Azure Event Grid
        ↓
(3) 분석/요약 처리
Azure Function + Azure OpenAI (GPT)
        ↓
(4) 알림 전송
Azure Logic Apps or Function → Teams/Slack/Email
```

------

## 🧩 필요한 Azure 구성 요소

| 구성 요소                                  | 설명                                           |
| ------------------------------------------ | ---------------------------------------------- |
| **Azure Monitor**                          | 로그 수집 및 KQL 쿼리 실행                     |
| **Log Analytics Alerts**                   | 에러 발생 감지 (예: 5분간 500번 에러 3건 이상) |
| **Azure Function**                         | 트리거 발생 시 GPT 호출 + 메시지 생성          |
| **Azure OpenAI Service**                   | 오류 메시지 요약, 담당자에게 보낼 메시지 생성  |
| **Azure Logic Apps / Teams/Slack Webhook** | 알림 메시지 전송                               |



------

## 🛠️ 예시 구현 흐름

### 1. **로그 수집 및 알림 조건 설정**

#### 예: 5분 내 500 에러가 3건 이상 발생 시 트리거

```
kql복사편집requests
| where resultCode == "500"
| where timestamp > ago(5m)
| summarize Count = count() by cloud_RoleName
| where Count > 3
```

- 이 조건을 Log Alert로 등록

------

### 2. **Azure Function에서 GPT로 요약 요청**

#### 오류 메시지 예시:

```
json복사편집[
  {
    "timestamp": "2025-07-02T08:31:00Z",
    "message": "NullReferenceException in UserController.cs line 42",
    "traceId": "abc123"
  },
  {
    "timestamp": "2025-07-02T08:32:10Z",
    "message": "NullReferenceException in UserController.cs line 42",
    "traceId": "abc125"
  }
]
```

#### GPT에게 전달할 프롬프트:

```
text복사편집다음은 최근 5분간 발생한 서버 오류입니다.
오류 유형, 발생 위치, 유사 원인 등을 요약해서 담당자에게 보고할 메시지를 만들어주세요.

<오류 목록>
- NullReferenceException in UserController.cs line 42 (2회)
- Trace ID: abc123, abc125
</오류 목록>
```

#### GPT 응답 예시:

> 🚨 **긴급 오류 발생 보고**
>  최근 5분간 `UserController.cs`의 42번째 줄에서 `NullReferenceException`이 2회 발생했습니다.
>  사용자 객체가 null인 상태로 `.Name` 속성에 접근한 것으로 추정됩니다.
>  빠른 확인 바랍니다.
>  🔍 관련 Trace ID: abc123, abc125

------

### 3. **Logic App으로 메시지 전송**

- Slack이나 Teams에 Webhook 연결
- 또는 Email, SMS 전송도 가능

```
json복사편집POST https://hooks.slack.com/services/XXX

{
  "text": "🚨 긴급 오류 발생\n최근 5분간 NullReferenceException 2회...\n담당자: @dev_ops"
}
```

------

## 📌 옵션 추가 기능

| 기능                  | 설명                                                         |
| --------------------- | ------------------------------------------------------------ |
| 담당자 매핑           | 특정 오류 코드나 서비스 별로 담당자 자동 지정 (예: `UserController` → A팀) |
| 해결 가이드 연결      | GPT가 오류 메시지를 기반으로 StackOverflow 유사 이슈 링크 포함 |
| Jira 티켓 자동 생성   | 오류 발생 시 티켓 자동 등록 (Logic App + Jira Connector)     |
| 슬랙/팀즈 명령어 대응 | “/최근오류” 요청 시 GPT가 요약된 장애 리포트 제공            |



------

## ✅ 구현 난이도 요약

| 항목                               | 난이도 | 비고                                |
| ---------------------------------- | ------ | ----------------------------------- |
| Azure Monitor 쿼리/Alert 설정      | 쉬움   | 포털에서 GUI 지원                   |
| Azure Function 작성 (Python/C#/JS) | 중간   | GPT 호출 포함                       |
| GPT 프롬프트 설계                  | 중간   | 정확한 요약 결과를 위해 테스트 필요 |
| Slack/Teams 연동                   | 쉬움   | Webhook만 등록하면 됨               |



------

## 🧪 샘플 코드 제공 원하시나요?

필요하시면 아래 중에서 제공해드릴게요:

- Azure Function 코드 (GPT 요청 포함)
- KQL 샘플 쿼리
- Slack Webhook 호출 스크립트
- GPT 프롬프트 템플릿



**++ 담당자 매핑 기능 / 내부 문서를 기반으로 한 해결 가이드 연결**



✅ **오류 로그 기반 자동 알림 및 지능형 대응 서비스**

## 🎯 **핵심 기능 요약**

1. **오류 감지**: 실시간으로 서버/서비스 오류 탐지
2. **GPT 요약**: 다건 오류를 정리·요약해 담당자가 한눈에 이해
3. **담당자 매핑**: 오류 유형 or 서비스 별로 자동 담당자 지정
4. **내부 문서 기반 해결 가이드 제공**
5. **자동 알림 전송**: Slack, Teams, Email 등으로 알림 발송

## 🧩 전체 아키텍처 구성

```
csharp복사편집[Azure Monitor / App Insights]
        ↓ (1. 오류 발생 감지)
[Log Alerts + KQL]
        ↓ (2. Alert Trigger)
[Azure Function]
 - 오류 수집
 - 담당자 매핑
 - GPT 요청 (OpenAI)
 - 해결 가이드 검색
        ↓ (3. 요약 + 문서 링크)
[Logic Apps / Webhook]
        ↓ (4. 알림 전송)
Slack / Teams / Email
```



## 🛠️ 상세 기능 설명

### ✅ 1. **오류 탐지 (Azure Monitor + KQL)**

- 예시 쿼리 (최근 5분 내 500번 오류 3건 이상):

```
kql복사편집requests
| where resultCode == "500"
| where timestamp > ago(5m)
| summarize Count = count() by cloud_RoleName
| where Count > 3
```

- 알림 기준을 Log Alert로 설정해 트리거

------

### ✅ 2. **Azure Function: 핵심 로직 처리**

#### 주요 역할:

- 오류 로그 수집
- **GPT에 오류 요약 요청**
- **오류 → 담당자 자동 매핑**
- **오류 키워드 기반 내부 문서 검색**
- Slack 등으로 최종 알림 포맷 구성

------

### ✅ 3. **담당자 매핑 기능**

#### 방식 1: 키워드 기반

```
python복사편집def get_responsible_person(error_message):
    if "UserController" in error_message:
        return "@team-user"
    elif "PaymentService" in error_message:
        return "@team-payment"
    return "@devops"
```

#### 방식 2: YAML/JSON 설정 파일

```
yaml복사편집error_mappings:
  - keyword: "UserController"
    owner: "@team-user"
  - keyword: "DBConnection"
    owner: "@team-db"
```

------

### ✅ 4. **내부 문서 기반 해결 가이드 연결**

#### 구현 방법:

- **Azure Cognitive Search**를 사내 문서 저장소 (PDF, MD, TXT 등)에 연결
- GPT가 오류 메시지로 **유사한 해결 문서 검색 요청**
- 결과 요약 + 링크 포함

#### 예시 프롬프트:

```
text복사편집이 오류 메시지와 관련된 사내 운영 문서 중 유사 해결 사례를 요약하고 링크를 알려줘.
에러: "NullReferenceException in UserController.cs line 42"
```

------

### ✅ 5. **GPT가 생성하는 최종 메시지 예시**

> 🚨 **[운영 오류 감지]**
>  지난 5분간 `UserController.cs`의 42번째 줄에서 `NullReferenceException`이 2회 발생했습니다.
>  추정 원인: 사용자 객체가 null 상태로 접근됨
>  담당자: @team-user
>
> 📄 **해결 가이드 문서**:
>  🔗 NullReference 오류 대응 가이드
>
> 🔍 Trace ID: abc123, abc125

------

### ✅ 6. **알림 전송 (Slack, Teams, Email 등)**

- Logic Apps or Azure Function에서 Webhook 호출
- 사용자 지정 메시지 형식 지원
- 클릭 시 관련 문서로 이동 가능



## 📦 개발 단위 별 역할 요약

| 컴포넌트      | 기술                          | 역할                             |
| ------------- | ----------------------------- | -------------------------------- |
| 로그 감지     | Azure Monitor + KQL           | 오류 발생 조건 탐지              |
| 트리거        | Log Alert / Event Grid        | Azure Function 호출              |
| 처리 로직     | Azure Function (Python/C#/JS) | GPT 호출, 담당자 매핑, 문서 검색 |
| 자연어 요약   | Azure OpenAI (GPT-4)          | 오류 요약 + 해결안 생성          |
| 해결문서 검색 | Azure Cognitive Search        | 내부 PDF, Markdown 등 검색       |
| 알림          | Logic Apps / Slack Webhook    | 최종 메시지 발송                 |

## ✔️ 도입 효과

| 항목              | 효과                                |
| ----------------- | ----------------------------------- |
| 장애 인지 속도    | 수동 모니터링 없이 즉시 탐지/요약   |
| 커뮤니케이션 효율 | 한 문장으로 요약된 알림 + 문서 첨부 |
| 운영 부담 감소    | 오류 triage와 문서 탐색 자동화      |

## 📌 필요 시 지원 가능

> 메모리에서 코드 확인

- GPT 프롬프트 설계 템플릿

- Azure Function 템플릿 코드

- 내부 문서 검색용 Cognitive Search 설정 예시

- Slack/Teams 알림 포맷 예제

  

✅ 마무리

이렇게 하면 시스템은 다음을 자동으로 처리합니다:

1. 오류 발생 시 실시간 탐지
2. GPT가 담당자에게 보낼 수준으로 요약
3. 내부 문서에서 유사 사례 검색 → 링크 포함
4. 담당자 지정 + Slack 알림 발송









