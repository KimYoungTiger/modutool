from app.models import Content
import urllib.request
import json

def perform_search_ranking_mystore(search_query, store_name, search_sort):

    client_id = "Zb7I1Pu79djcliEgfoNE"
    client_secret = "IIstjX5_Yp"
    encText = urllib.parse.quote(search_query)
    display = 100

    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&sort=" + search_sort # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    count = 1
    
    if(rescode==200):   #200 성공일경우
        response_body = response.read()
        results = json.loads(response_body.decode('utf-8'))
        for item in results['items']:
            if item['mallName'] == store_name:
                return_value = str(count)
                break
            count += 1
            if results['total'] == count:
                return_value = '검색 순위에 없습니다.'
                break
    else:
        return_value = "Error Code:" + rescode
        
    return return_value


def perform_list_product(store_name, search_sort, search_count):
    
    # 검색 로직 구현
    client_id = "Zb7I1Pu79djcliEgfoNE"
    client_secret = "IIstjX5_Yp"
    encText = urllib.parse.quote(store_name)
    display = search_count

    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&sort=" + search_sort # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        results = json.loads(response_body.decode('utf-8'))
        return_value = [{'title': item['title'], 'lprice':item['lprice'], 'link': item['link']} for item in results['items']]
    else:
        return_value ="Error Code:" + rescode
        
    return return_value



def perform_search_ranking_store(search_query, search_sort, search_count):

    client_id = "Zb7I1Pu79djcliEgfoNE"
    client_secret = "IIstjX5_Yp"
    encText = urllib.parse.quote(search_query)
    display = search_count

    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&sort=" + search_sort # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        results = json.loads(response_body.decode('utf-8'))
        return_value = [{'title': item['title'], 'lprice':item['lprice'], 'link': item['link']} for item in results['items']]
    else:
        return_value ="Error Code:" + rescode
        
    return return_value
