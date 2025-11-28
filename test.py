import requests, os
from dotenv import load_dotenv

load_dotenv()


NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_URL = "https://openapi.naver.com/v1/search/news.json"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


query = 'ssafy'

if query:
    # 검색어가 있다면
    headers = {
        "X-Naver-Client-Id" : NAVER_CLIENT_ID,
        "X-Naver-Client-Secret" : NAVER_CLIENT_SECRET
    }

    params = {
        "query" : query,
        "display" : 10,
        "sort" : "sim",
    }

    response = requests.get(NAVER_URL, headers=headers, params=params)
    if response.status_code == 200:
        # 성공인 경우
        data = response.json()
        print(response)
        print(data)
        print(data.get('items'))
    else:
        print('에러')
else:
    print('검색어 없음')
