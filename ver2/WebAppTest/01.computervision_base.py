import requests

# 사이트 가져오기
response = requests.get("http://www.naver.com")
print('\n', response.status_code, '\n', response.text[:50])

# 이미지 가져오기
response = requests.get("https://search.pstatic.net/sunny/?src=https%3A%2F%2Fcbsnews2.cbsistatic.com%2Fhub%2Fi%2Fr%2F2021%2F03%2F25%2F0437e6b8-cbd2-482f-a395-89c0af6bdd68%2Fthumbnail%2F1200x630%2F8f921f538f360dfd03fc80000fbb538b%2F0910-birdextinction-275366-640x360.jpg&type=sc960_832")
print('\n', response.content[:50]) # b : binary / x~ : 16진수 -> 받아서 binary로 복원해서 사용해야 함



