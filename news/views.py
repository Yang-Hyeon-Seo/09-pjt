from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import SearchForm
from .models import News
from .serializers import NewsSerializer

import requests, os
from dotenv import load_dotenv


load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_URL = "https://openapi.naver.com/v1/search/news.json"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@api_view(['GET'])
def index(request):
    form = SearchForm()
    saved_news = News.objects.all()

    # print(saved_news)
    context = {
        'form' : form,
        'saved_news' : saved_news,
    }
    return render(request, 'news/index.html', context)

def search(request):
    print(request.method)
    saved_news = News.objects.all()
    serializer = NewsSerializer(saved_news, many=True)

    if request.method == "GET":
        query = request.GET.get('query')  # 검색어로 입력한 단어 가져오기
        print(query)

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
                # print(response)
                # print(data)
                # print(data.get('items'))
                items = data.get('items')

                # 데이터 저장하기
                for item in items:
                    title = item['title']
                    link = item['link']
                    description = item['description']

                    if not News.objects.filter(title=title).exists():
                        News.objects.create(
                            title=title,
                            link=link,
                            description=description
                        )

            else:
                print('에러')
        else:
            print('검색어 없음')
            news = News.objects.all()
    else:
        print('get아님')
    return Response(serializer.data)
    # return redirect('news:index')

def get_data(request):
    print('DB 조회')
    db = News.objects.all()
    print(db.data)
    # datas = []
    # for data in db:
    #     title = data['title']
    #     link = data['link']
    #     description = data['description']

    #     datas.append({
    #         'id'
    #     })
    # return Response()

    pass