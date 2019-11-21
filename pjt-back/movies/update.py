from decouple import config
import requests
import datetime
from pprint import pprint
import bs4

key = config('API_KEY')
BASE_URL = config('BASE_URL')

HEADERS = {
    'X-Naver-Client-Id' : config('CLIENT_ID'),
    'X-Naver-Client-Secret' : config('CLIENT_SECRET'),
}
NAVER_BASE_URL = config('NAVER_BASE_URL')

for week_ago in range(1, 2):
    targetDt = datetime.date.today() - datetime.timedelta(weeks=week_ago)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url =f'{BASE_URL}boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'

    response = requests.get(api_url).json()['boxOfficeResult']['weeklyBoxOfficeList']
    
    for movie in response:
        movieCd = movie['movieCd']
        audiAcc = movie['audiAcc']
        
        #영화 상세정보 들어가기
        detail_url = f'{BASE_URL}movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
        movie_info = requests.get(detail_url).json()['movieInfoResult']['movieInfo']
        # pprint(movie_info)
        movieNm = movie_info['movieNm']
        prdtYear = movie_info['prdtYear']
        genres = movie_info['genres']

        directors = movie_info['directors']
        actors = movie_info['actors']
        # [{'peopleNm' : '조진웅'}, {}]

        watchGradeNm = movie_info['audits'][0]['watchGradeNm']



        #네이버 영화 상세정보 들어가기 -> 네이버 영화 api에서 영화포스터 가져오고, 네이버영화 홈페이지 링크를 갖고오기위하여 필요함.
        naver_url = f'{NAVER_BASE_URL}?query={movieNm}&yearfrom={prdtYear}&yearto={prdtYear}'
        movie_naver_detail = requests.get(naver_url, headers=HEADERS).json()
        # pprint(movie_naver_detail)
        movie_link = movie_naver_detail['items'][0]['link'].replace('basic', 'detail')
        post_url = movie_naver_detail['items'][0]['image']
        userRating = movie_naver_detail['items'][0]['userRating']

        html = requests.get(movie_link+'#tab').text
        naver_movie = bs4.BeautifulSoup(html, 'html.parser')
        naver_movie = naver_movie.select_one('.lst_people')

        for actor in actors + directors:
            peopleNm = actor['peopleNm']
            
            img_tag = naver_movie.select_one(f'img[alt="{peopleNm}"]')
            img_url = 'person_base.jpg'
            for string in str(img_tag).split():
                if string[:3] == 'src':
                    # print(string.split('jpg')[0][5:] + 'jpg')
                    img_url = string.split('jpg')[0][5:] + 'jpg'

            actor_detail_url = f'{BASE_URL}/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}&filmoNames={movieNm}'
            actor_detail = requests.get(actor_detail_url).json()['peopleListResult']['peopleList'][0]

            peopleCd = actor_detail['peopleCd']
            actor['id'] = id
            print(peopleCd)

        break