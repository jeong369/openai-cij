import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main() :

    # Clear the console screen : nt=Windows, posix=Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get environment variables
    load_dotenv()

    # Settings for Azure OpenAI and Azure Cognitive Search
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_endpoint = os.getenv('OPENAI_ENDPOINT')
    chat_deployment_name = os.getenv('CHAT_DEPLOYMENT_NAME') # 채팅 모델 배포 이름
    embedding_deployment_name = os.getenv('EMBEDDING_DEPLOYMENT_NAME') # 임베딩 모델 배포 이름
    search_api_key = os.getenv('SEARCH_API_KEY') # Azure Cognitive Search API 키
    search_endpoint = os.getenv('SEARCH_ENDPOINT') # Azure Cognitive Search 엔드포인트
    search_index_name = os.getenv('SEARCH_INDEX_NAME') # Azure Cognitive Search 인덱스 이름

    # Initialize Azure OpenAI client
    chat_client = AzureOpenAI(
        api_key=openai_api_key,
        api_version='2024-12-01-preview',  # OpenAI API 버전
        azure_endpoint=openai_endpoint,
        # deployment_name=chat_deployment_name,
    )

    # Initialize prompt with system message
    prompt = [
        {
            "role": "system",
            "content": "You are a travel assistant that provides information about travel destinations, including popular attractions, local cuisine, and cultural experiences."
        }
    ]

    while True:
        input_text = input("Enter your qeustion (or type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            print("Exiting the application.")
            break
        elif input_text.strip() == "" :
            print("Please enter a valid question.")
            continue
        else:
            # Add user input to the prompt
            prompt.append({"role": "user", "content": input_text})

            # Additional parameters to apply RAG pattern using the AI Search index
            # -- 실제 데이터는 storage 에 있지만, 우리가 사용하는건 AI Search
            rag_params = {
                "data_sources": [
                    {
                        "type": "azure_search",
                        "parameters": {
                            "endpoint": search_endpoint,
                            "index_name": search_index_name,
                            "authentication": {
                                "type": "api_key",
                                "key": search_api_key
                            },
                            "query_type": "vector",
                            "embedding_dependency": {
                                "type": "deployment_name",
                                "deployment_name": embedding_deployment_name,
                            }
                        }
                    }
                ]
            }

            # submit the prompt to the chat client
            response = chat_client.chat.completions.create(
                model=chat_deployment_name,
                messages=prompt,
                extra_body=rag_params,
            )

            completion = response.choices[0].message.content
            print(f"AI Response : {completion}")

            # 대화 누적 필요
            prompt.append({"role": "assistant", "content": completion})




if __name__=='__main__' :
    main()