
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


# OPENAI API 호출 예시
response = openai.chat.completions.create(
    model = "dev-gpt-4o-mini-cj", # 배포이름
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "OpenAI에 대해서 설명해줘",
        }
    ],
    # stream=True
)

# 응답출력 - 기본
# print(response)
print(response.choices[0].message.content)

# 응답출력 - 긴 응답 기다리지 않고 응답 스트림 출력
# for update in response:
#     if update.choices:
#         print(update.choices[0].delta.content or "", end="")