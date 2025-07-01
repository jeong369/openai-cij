
import openai
import os
from dotenv import load_dotenv


# 환경변수 로딩
load_dotenv()


# 환경변수가 같은 파일에 있을 경우
'''
openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = AZURE_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION
'''

# 환경변수 로딩 시, 
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

print(openai.api_key)
print(openai.azure_endpoint)
print(openai.api_type)
print(openai.api_version)

subject = input("시의 주제를 입력하세요 : ")
content = input("시의 내용을 입력하세요 : ")


# OPENAI API 호출 예시
response = openai.chat.completions.create(
    model = "dev-gpt-4o-mini-cj", # 배포이름
    messages=[
        {"role": "system", "content": "You are a AI porm generator.",},
        {"role": "user", "content": "시의 주제는 " + subject,},
        {"role": "user", "content": "시의 내용은 " + content,},
        {"role": "user", "content": "이 내용으로 시를 써줘"},
    ],
    temperature=0.9, # 0(T와 가까움) ~ 1(F와 가까움) : 1로 가까울수록 학습되어진 내용에 영향을 많이 받아서 응답을 출력함.
    max_tokens=500, # 정해진 토큰 내에서 만들어내야, 운영비용 예측이 가능함.
)

# 응답출력 - 기본
# print(response)
print(response.choices[0].message.content)

# 응답출력 - 긴 응답 기다리지 않고 응답 스트림 출력
# for update in response:
#     if update.choices:
#         print(update.choices[0].delta.content or "", end="")