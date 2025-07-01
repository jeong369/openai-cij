import requests

SUBSCRIPTION_KEY = "FOXijx2exxHmQF7E2TCwGSQeXuCRbyHBU9vRI1ypSvxvDXDVV9lfJQQJ99BGACYeBjFXJ3w3AAAFACOGDO46"
ENDPOINT = "https://user24-computervision-001.cognitiveservices.azure.com/"

# 이미지 분석
def analyze_image(image_path) :
    ENDPOINT_URL = ENDPOINT + "vision/v3.2/analyze"

    # 변수 설정
    params = {"visualFeatures" : "Categories,Description,Color"}
    headers = {
        "Ocp-Apim-Subscription-Key" : SUBSCRIPTION_KEY,
        "Content-Type" : "application/octet-stream"
    }

    # 파일 읽어오기
    try :
        with open(image_path, "rb") as image_file:  # r:read, b:binary type
            image_data = image_file.read()
            
    except Exception as e :
        print(f"Error reading image file : {e}")
        return None
    
    # 응답 출력
    response = requests.post(ENDPOINT_URL, params=params, headers=headers, data=image_data)
    if response.status_code == 200 :
        analysis = response.json()
        return analysis
    else:
        print(f"Error : {response.status_code} - {response.text}")
        return None

# OBJECT DETECTION

# OCR


def main():
    image_path = input("Enter the path to the image file : ")

    result = analyze_image(image_path)
    if result :
        print("Analysis Result : ")
        print(result)


if __name__ == '__main__':
    main()