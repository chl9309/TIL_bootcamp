# 02_pjt

> 공통 요구사항

- 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 필요한 영화 데이터를 수집하는 과정입니다. 
- 완성된 기능들은 향후 커뮤니티 서비스에서 활용할 수 있습니다. 
- API 요청 시 언어 및 지역 설정 데이터는 한국을 기준으로 합니다.



### A. 인기 영화 조회(problem_a)

> 인기 영화 목록을 응답 받아 개수를 출력

#### code

```python
import requests

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.
    apikey = 'd6f2a85b7a18b491974d06bcffe4c61c'

    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko-KR&page=1'
    response = requests.get(URL).json()
    count = 0
    for i in range(len(response['results'])):
         count +=1
    return count

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
```

TMDB에서 `api`발급받아 requests 라이브러리를 사용하여 TMDB에서 현재 인기 있는 영화 목록 `Get Popular`데이터를 요청하면 딕셔너리 형태로 데이터를 받게 되는데 여기서 `results`에 해당하는 value의 길이만큼 반복하여 카운트를 증가 시킨다.

#### 어려웠던 점 및 해결방안

JSONViewer 가 작동하지 않아 value를 찾기 어려웠다. 하지만 영화제목 개수를 세면 된다는 아이디어를 가지고 괄호와 콜론등을 확인하며 results키를 찾았으며 반복문을 활용하여 카운트 하였다.

---

### B. 특정 조건에 맞는 인기 영화 조회 1 (problem_b)

> 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력

#### code

```python
import requests
from pprint import pprint


def vote_average_movies():
    pass 
    # 여기에 코드를 작성합니다.  
    apikey = 'd6f2a85b7a18b491974d06bcffe4c61c'

    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko-KR&page=1'
    response = requests.get(URL).json()
    high_vote = []
    for i in range(len(response['results'])):
      if response['results'][i]['vote_average'] >= 8:
        high_vote.append(response['results'][i])
    
    return high_vote

    # if response['results'][0]['vote_average'] >= 8:
    #   return response

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """

```

영화목록(20개)을 반복하기 위해 반복문을 마찬가지로 사용하였으며 내부 딕셔너리 중 `vote_average`가 8점 이상인 목록을 추출하기 위해 조건문을 작성하였다. 이때 평점이 8점 이상인 영화들의 리스트를 high_vote로 설정하여 8점이 넘는다면 .append()를 활용하여 vote_average가 8점 이상인 영화들을 리스트에 추가하였다.



### C. 특정 조건에 맞는 인기 영화 조회 2 (problem_c)

> 인기 영화 목록 평점 상위 5개 출력

#### code

```python
import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.
    apikey = 'd6f2a85b7a18b491974d06bcffe4c61c'

    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko-KR&page=1'
    response = requests.get(URL).json()
    high_vote = []
    new = []
    for i in range(len(response['results'])):
        high_vote.append(response['results'][i]['vote_average'])
    a = sorted(high_vote)
    
    for i in range(len(response['results'])):
        if response['results'][i]['vote_average'] >= a[-5]:
            new.append(response['results'][i])
    
    return new

    return a[-5]
    
 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """

```

영화 리스트를 받아와서 `vote_average`를 추출한 값을 새로운 high_vote 리스트에 담은 다음 정렬한 값을 a에 할당한다. 상위 5개를 추출해야 하므로 리스트 a를 인덱싱하여 상위 5번째 값과 데이터의 값을 비교하여 5번째보다 크면 반환한다.

#### 어려웠던 점 및 해결방안

딕셔너리 내부에 평점이 있어서 평점 순서대로 sorted 하는것이 어려웠다. 그래서 평점만 따로 추출하여 상위 5번째의 값을 가져와 problem_b처럼 조건문을 활용하여 해결하였다. 딕셔너리 내부에 있는 키값에 해당하는 벨류를 sorted 하는 방법을 배워야 겠다.



### D. 특정 추천 영화 조회 (problem_d)

> 제공된 영화 제목을 검색하여 추천 영화 목록 출력

#### code

```python
import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.
    api_key = 'd6f2a85b7a18b491974d06bcffe4c61c'
    URL_1 = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KR&query={title}&page=1&include_adult=false'
    response_search = requests.get(URL_1).json()
    if response_search['results'] == []:
        return None

    movie_id = response_search['results'][0]['id']
    URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KR&page=1'
    response_recommendations = requests.get(URL_2).json()

    name = []
    for i in range(len(response_recommendations['results'])):
        name.append(response_recommendations['results'][i]['title'])
    
    return name

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

```

Search Movies api를 통해 함수에 정의된 title을 검색한다. 이 때 title이 검색할 수 없는 경우라면 `None`을 반환해야 하기 때문에 조건문을 사용하여 result가 빈 리스트이면 `None`을 반환하도록 한다.

영화 검색 api로 부터 영화 id를 movie_id 변수로 선언하여 추천 영화 목록 api에서 검색하도록 한다.

추천 영화를 받기 위한 리스트 name을 선언하고 추천 영화의 제목만 제목만 인덱싱 한다.



#### 어려웠던 점 및 해결방안

처음 영화 검색 api 사용방법이 서툴러 query가 없다는 오류가 나타났었는데 여기에 title이 들어가야 함을 깨닫는데 오래 걸렸다. 그래서 옆 동기들에게 도움을 받았다.

그 다음 None을 출력하기 위해 반복문을 사용해야 하는데 위치를 어디로 설정해야 할지 고민하는데 오래걸렸다.

애초에 영화검색에서 검색되지 않으면 None이 리턴되도록 하면 되는데 코드가 길어지다 보니 아래쪽에서 None을 출력하기 위한 코드 작성을 고민하고 있었다. 코드를 더욱 폭넓게 보고 문제 이해 능력을 길러야 겠다.



### E. 출연진, 연출진 데이터 조회 (problem_e)

> 제공된 영화 제목을 검색하여 해당 영화의 출연진(cast), 그리고 스태프(crew) 중 연출진 목록만을 출력

#### Code

```python
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    api_key = 'd6f2a85b7a18b491974d06bcffe4c61c'
    URL_1 = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KR&query={title}&page=1&include_adult=false'
    response_search = requests.get(URL_1).json()
    if response_search['results'] == []:
        return None

    movie_id = response_search['results'][0]['id']
    URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-KR'
    response_Credit = requests.get(URL_2).json()
    chool = []
    gam = []
    for i in range(len(response_Credit['cast'])):
        if response_Credit['cast'][i]['cast_id'] < 10:
            chool.append(response_Credit['cast'][i]['name'])
    for j in range(len(response_Credit['crew'])):
        if response_Credit['crew'][j]['department'] == 'Directing':
            gam.append(response_Credit['crew'][j]['name'])
    dict_a = {
        'cast' : chool,
        'directing' : gam
    }

    return dict_a
    # chool = []
    # if response_Credit['cast'][0]['cast_id'] < 10:
    #     chool.append()
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

```

movie_id를  가져와서 출연진과 연출진을 조회하기 위해 chool, gam 리스트를 선언하여 각각에 선언한다.

chool리스트에는 `cast_id`가 10미만인 사람들만 넣기 위해 조건문을 이용하였으며 연출진도 마찬가지로 `Directing`인 사람들만 리스트에 넣기 위해 조건문을 이용하였다. 출력이 딕셔너리 형태로 나타났기 때문에  딕셔너리의 value값으로 chool, gam을 넣어주었다.



#### 어려웠던 점 및 해결방안

Directing을 추출하는 과정에서 키 값인 known_for_department가 가지고 있는 value가 Directing을 추출하였었는데 해당 시도 결과 봉준호 감독은 4번이나 중복으로 출력되게 되었다. 다시 데이터를 조회 하여 보니 `department`의 value 값이 각 감독마다 하나씩 가지고 있다는 것을 알아내어 인덱싱 하는데 문제점을 해결하였다.



