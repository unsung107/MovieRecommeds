from .models import Movie, Review, Recommend, Actor, Director, CommingMovie, Genre, RecommendReview, MovieComment
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer, DirectorSerializer, RecommendSerializer, UserSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import ReviewCreationForm, RecommendReviewCreationForm
from pprint import pprint
from decouple import config
import requests
import datetime
import bs4
User = get_user_model()

def findmovieupdate(request, movie_nm):
    
    key = config('API_KEY')
    BASE_URL = config('BASE_URL')

    HEADERS = {
        'X-Naver-Client-Id' : config('CLIENT_ID'),
        'X-Naver-Client-Secret' : config('CLIENT_SECRET'),
    }
    NAVER_BASE_URL = config('NAVER_BASE_URL')

    api_url =f'{BASE_URL}movie/searchMovieList.json?key={key}&movieNm={movie_nm}'
    print(api_url)
    response = requests.get(api_url).json()['movieListResult']['movieList']
    for movie in response:
        
        try:
            movieCd = movie['movieCd']
            if Movie.objects.filter(code=f'{movieCd}'):
                print('넘어갑니다')
                continue
            
            
            #영화 상세정보 들어가기
            detail_url = f'{BASE_URL}movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
            
            movie_info = requests.get(detail_url).json()['movieInfoResult']['movieInfo']
            movieNm = movie_info['movieNm']
            prdtYear = movie_info['prdtYear']
            genres = movie_info['genres']

            for genre in genres:
                genreNm = genre['genreNm']
                temp_genre = Genre()
                temp_genre.name = genreNm
                try:
                    temp_genre.save()
                    genre['id'] = temp_genre.id
                except:
                    temp_genre = get_object_or_404(Genre, name=f'{genreNm}')
                    genre['id'] = temp_genre.id
                    continue

            directors = movie_info['directors']
            actors = movie_info['actors']
            # [{'peopleNm' : '조진웅'}, {}]
            if movie_info['audits']:
                watchGradeNm = movie_info['audits'][0]['watchGradeNm']
            else:
                watchGradeNm = ''

            if watchGradeNm == '15세이상관람가':
                watchgrade = 15
            elif watchGradeNm == '12세이상관람가':
                watchgrade = 12
            elif watchGradeNm == '중학생이상관람가':
                watchgrade = 14
            elif watchGradeNm == '청소년관람불가':
                watchgrade = 20
            elif watchGradeNm == '전체관람가':
                watchgrade = 0
            else:
                watchgrade = 0



            #네이버 영화 상세정보 들어가기 -> 네이버 영화 api에서 영화포스터 가져오고, 네이버영화 홈페이지 링크를 갖고오기위하여 필요함.
            naver_url = f'{NAVER_BASE_URL}?query={movieNm}&yearfrom={prdtYear}&yearto={prdtYear}'
            movie_naver_detail = requests.get(naver_url, headers=HEADERS).json()
            if not movie_naver_detail['items']:
                print('네이버 정보가 없네요 : ', movieNm)
                continue
            movie_link = movie_naver_detail['items'][0]['link'].replace('basic', 'detail')
            print(movieNm)
            post_url = '../assets/base_poster.jpg'
            post_url = movie_naver_detail['items'][0]['image']
            
            userRating = movie_naver_detail['items'][0]['userRating']

            discription_html = requests.get(movie_naver_detail['items'][0]['link']).text
            discription_page = bs4.BeautifulSoup(discription_html, 'html.parser')
            discription = discription_page.select_one(f'p[class="con_tx"]')
            if discription:
                discription = discription.text
            else:
                discription = ''
            
            html = requests.get(movie_link+'#tab').text
            naver_movie = bs4.BeautifulSoup(html, 'html.parser')
            
            naver_movie = naver_movie.select_one('.lst_people')
            

            for person in actors + directors:
                peopleNm = person['peopleNm']
                img_url = '../assets/base_person.jpg'

                if naver_movie:
                    img_tag = naver_movie.select_one(f'img[alt="{peopleNm}"]')
                    
                    for string in str(img_tag).split():
                        if string[:3] == 'src':
                            img_url = string.split('jpg')[0][5:] + 'jpg'

                person_detail_url = f'{BASE_URL}/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}&filmoNames={movieNm}'
                people_list = requests.get(person_detail_url).json()['peopleListResult']
                if not people_list:
                    print('이사람 없어요 : ', peopleNm)
                person_detail = people_list['peopleList'][0]

                peopleCd = person_detail['peopleCd']
                if person in actors:
                    temp_person = Actor()
                else:
                    temp_person = Director()
                temp_person.name = peopleNm
                temp_person.code = peopleCd
                temp_person.image_url = img_url
                try:
                    temp_person.save()
                except:
                    if person in actors:
                        target_person = get_object_or_404(Actor, code=peopleCd)
                    else:
                        target_person = get_object_or_404(Director, code=peopleCd)
                    person['id'] = target_person.id
                    continue
                person['id'] = temp_person.id

            temp_movie = Movie()
            temp_movie.title = movieNm
            temp_movie.code = movieCd
            temp_movie.audience = audiAcc
            temp_movie.post_url = post_url
            temp_movie.score = float(userRating)
            temp_movie.watch_grade = watchgrade
            temp_movie.watch_grade_name = watchGradeNm
            temp_movie.discription = discription
            try:
                temp_movie.save()
            except:
                temp_movie = get_object_or_404(Movie, code = movieCd)
                if int(temp_movie.audience) < int(audiAcc):
                    temp_movie.audience = audiAcc
                    temp_movie.save()
                
            for actor in actors:
                target_actor = get_object_or_404(Actor, pk=actor['id'])
                temp_movie.actors.add(target_actor)
            
            for director in directors:
                target_director = get_object_or_404(Director, pk=director['id'])
                temp_movie.directors.add(target_director)
            
            for genre in genres:
                target_genre = get_object_or_404(Genre, pk=genre['id'])
                temp_movie.genres.add(target_genre)
        except:
            continue


    movies = Movie.objects.all()
    context = {
        'movies': movies.count()
    }
    return JsonResponse(context)


def commingmovieupdate(request):
    URL = config('COMMING_MOVIE_URL')
    
    html = requests.get(URL).text
    comming_dates = bs4.BeautifulSoup(html, 'html.parser')
    comming_dates = comming_dates.select('.lst_wrap')
    today = datetime.date.today()

    for comming_date in comming_dates:
        comming_movies = comming_date.select('li')
        
        for comming_movie in comming_movies:
            post_url = '../assets/base_poster.jpg'
            img_tag = comming_movie.select_one('img')
            for string in str(img_tag).split():
                if string[:3] == 'src':
                    post_url = string.split('jpg')[0][5:] + 'jpg'
            
            openDt = ''.join(comming_movie.select_one('.lst_dsc .info_txt1 dd').text.split()[-2].split('.'))
            title = comming_movie.select_one('.tit').a.text
            
            openDt = int(openDt)
            if openDt < 10000000:
                openDt *= 100
                openDt += 1
            openDt = datetime.date(openDt // 10000, openDt // 100 % 100, openDt % 100)
            print(openDt, title)
            temp_comming_movie = CommingMovie()
            temp_comming_movie.title = title
            temp_comming_movie.openDt = openDt
            temp_comming_movie.post_url = post_url
            try:
                temp_comming_movie.save()
            except:
                continue
                


        
    return JsonResponse({'commingMovies': CommingMovie.objects.all().count()})


# @require_POST
def movieupdate(request):
    print('start')
    
    key = config('API_KEY')
    BASE_URL = config('BASE_URL')

    HEADERS = {
        'X-Naver-Client-Id' : config('CLIENT_ID'),
        'X-Naver-Client-Secret' : config('CLIENT_SECRET'),
    }
    NAVER_BASE_URL = config('NAVER_BASE_URL')

    for week_ago in range(4,6):
        print(week_ago)
        targetDt = datetime.date.today() - datetime.timedelta(weeks=week_ago)
        targetDt = targetDt.strftime('%Y%m%d')
        api_url =f'{BASE_URL}boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'

        response = requests.get(api_url).json()['boxOfficeResult']['weeklyBoxOfficeList']
        for movie in response:
            try:
                movieCd = movie['movieCd']
                if Movie.objects.filter(code=f'{movieCd}'):
                    print('넘어갑니다')
                    continue
                audiAcc = movie['audiAcc']
                
                #영화 상세정보 들어가기
                detail_url = f'{BASE_URL}movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
                movie_info = requests.get(detail_url).json()['movieInfoResult']['movieInfo']
                movieNm = movie_info['movieNm']
                prdtYear = movie_info['prdtYear']
                genres = movie_info['genres']

                for genre in genres:
                    genreNm = genre['genreNm']
                    temp_genre = Genre()
                    temp_genre.name = genreNm
                    try:
                        temp_genre.save()
                        genre['id'] = temp_genre.id
                    except:
                        temp_genre = get_object_or_404(Genre, name=f'{genreNm}')
                        genre['id'] = temp_genre.id
                        continue
                kmdb = requests.get(KMDB_BASE_URL + KMDB_API_KEY + 'title=' + movieNm).json()
                directors = movie_info['directors']
                actors = movie_info['actors']
                # [{'peopleNm' : '조진웅'}, {}]
                if movie_info['audits']:
                    watchGradeNm = movie_info['audits'][0]['watchGradeNm']
                else:
                    watchGradeNm = ''

                if watchGradeNm == '15세이상관람가':
                    watchgrade = 15
                elif watchGradeNm == '12세이상관람가':
                    watchgrade = 12
                elif watchGradeNm == '중학생이상관람가':
                    watchgrade = 14
                elif watchGradeNm == '청소년관람불가':
                    watchgrade = 20
                elif watchGradeNm == '전체관람가':
                    watchgrade = 0
                else:
                    watchgrade = 0



                #네이버 영화 상세정보 들어가기 -> 네이버 영화 api에서 영화포스터 가져오고, 네이버영화 홈페이지 링크를 갖고오기위하여 필요함.
                naver_url = f'{NAVER_BASE_URL}?query={movieNm}&yearfrom={prdtYear}&yearto={prdtYear}'
                movie_naver_detail = requests.get(naver_url, headers=HEADERS).json()
                if not movie_naver_detail['items']:
                    print('네이버 정보가 없네요 : ', movieNm)
                    continue
                movie_link = movie_naver_detail['items'][0]['link'].replace('basic', 'detail')
                snapshot_link = movie_naver_detail['items'][0]['link'].replace('basic', 'photoView')
                video_link = movie_naver_detail['items'][0]['link'].replace('basic', 'media')
                print(movieNm)
                post_url = 'https://ssl.pstatic.net/static/movie/2012/06/dft_img111x139.png'
                
                
                userRating = movie_naver_detail['items'][0]['userRating']

                discription_html = requests.get(movie_naver_detail['items'][0]['link']).text
                discription_page = bs4.BeautifulSoup(discription_html, 'html.parser')
                discription = discription_page.select_one(f'p[class="con_tx"]')
                if discription:
                    discription = discription.text
                else:
                    discription = ''
                
                post_tag = str(discription_page.select_one('.wide_info_area .poster a img')).split()

                for string in post_tag:
                    if string[:3] == 'src':
                        if 'jpg' in string:
                            post_url = string.split('jpg')[0][5:] + 'jpg'
                        elif 'png' in string:
                            post_url = string.split('png')[0][5:] + 'png'

                html = requests.get(movie_link+'#tab').text
                naver_movie = bs4.BeautifulSoup(html, 'html.parser')
                
                naver_movie = naver_movie.select_one('.lst_people')
                
                snapshot_html = requests.get(snapshot_link).text
                snapshot_page = bs4.BeautifulSoup(snapshot_html, 'html.parser')
                snapshots = str(snapshot_page.select_one('.list_area .rolling_list ul')).split('</li>')
                snapshot_list = []
                for snapshot in snapshots:
                    if 'STILLCUT' in snapshot:
                        snapshot_list.append(snapshot)
                snapshot_url = ''
                for snapshot in snapshot_list:
                    snapshot = snapshot.split()
                    for string in snapshot:
                        if string[:3] == 'src':
                            if 'jpg' in string:
                                snapshot_url += string.split('jpg')[0][5:] + 'jpg, '
                            elif 'png' in string:
                                snapshot_url = string.split('png')[0][5:] + 'png, '

                if snapshot_url:
                    snapshot_url = snapshot_url[:-2]

                video_html = requests.get(video_link).text
                video_page = bs4.BeautifulSoup(video_html, 'html.parser')
                videos = str(video_page.select_one('.video_thumb')).split('</li>')
                video_url = ''
                for video in videos:
                    if '메인 예고편' in video:
                        video_url = video
                video_url = video_url.split()
                video_href = ''
                for string in video_url:
                    if 'href' in string:
                        video_href = string[6:-1]
                if video_href:
                    video_href = 'https://movie.naver.com' + video_href

                    video_html = requests.get(video_href).text
                    video_page = bs4.BeautifulSoup(video_html, 'html.parser')
                    videos = str(video_page.select_one('iframe')).split()

                    for string in videos:
                        if 'videoPlayer' in string:
                            video_url = 'https://movie.naver.com' + string[5:-8] + '330x240'
                            video_url = video_url.replace('amp;', '')
                else:
                    video_url = ''

                for person in actors + directors:
                    peopleNm = person['peopleNm']
                    img_url = 'https://ssl.pstatic.net/static/movie/2012/06/dft_img111x139.png'

                    if naver_movie:
                        img_tag = naver_movie.select_one(f'img[alt="{peopleNm}"]')
                        
                        for string in str(img_tag).split():
                            if string[:3] == 'src':
                                if 'jpg' in string:
                                    img_url = string.split('jpg')[0][5:] + 'jpg'
                                elif 'png' in string:
                                    img_url = string.split('png')[0][5:] + 'png'

                    person_detail_url = f'{BASE_URL}/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}&filmoNames={movieNm}'
                    people_list = requests.get(person_detail_url).json()['peopleListResult']
                    if not people_list:
                        print('이사람 없어요 : ', peopleNm)
                    person_detail = people_list['peopleList'][0]

                    peopleCd = person_detail['peopleCd']
                    if person in actors:
                        temp_person = Actor()
                    else:
                        temp_person = Director()
                    temp_person.name = peopleNm
                    temp_person.code = peopleCd
                    temp_person.image_url = img_url
                    try:
                        temp_person.save()
                    except:
                        if person in actors:
                            target_person = get_object_or_404(Actor, code=peopleCd)
                        else:
                            target_person = get_object_or_404(Director, code=peopleCd)
                        person['id'] = target_person.id
                        continue
                    person['id'] = temp_person.id

                temp_movie = Movie()
                temp_movie.title = movieNm
                temp_movie.code = movieCd
                temp_movie.audience = audiAcc
                temp_movie.post_url = post_url
                temp_movie.score = float(userRating)
                temp_movie.watch_grade = watchgrade
                temp_movie.watch_grade_name = watchGradeNm
                temp_movie.discription = discription
                temp_movie.snapshot_url = snapshot_url
                temp_movie.video_url = video_url
                
                try:
                    temp_movie.save()
                except:
                    temp_movie = get_object_or_404(Movie, code = movieCd)
                    if int(temp_movie.audience) < int(audiAcc):
                        temp_movie.audience = audiAcc
                        temp_movie.save()
                    
                for actor in actors:
                    target_actor = get_object_or_404(Actor, pk=actor['id'])
                    temp_movie.actors.add(target_actor)
                
                for director in directors:
                    target_director = get_object_or_404(Director, pk=director['id'])
                    temp_movie.directors.add(target_director)
                
                for genre in genres:
                    target_genre = get_object_or_404(Genre, pk=genre['id'])
                    temp_movie.genres.add(target_genre)
            except:
                print('error')
                continue


    movies = Movie.objects.all()
    context = {
        'movies': movies.count()
    }
    return JsonResponse(context)

def homemovielist(request, genre_id):
    
    genre = get_object_or_404(Genre, pk=genre_id)
    serializer = GenreSerializer(instance=genre)
    return JsonResponse(serializer.data)

def searchMovie(request, movie_nm):
    if movie_nm == ' ':
        return JsonResponse({'movies': []})
    
    movies = Movie.objects.filter(title__icontains=movie_nm)
    
    serializer = MovieSerializer(instance=movies, many=True)
    pprint(serializer.data)
    return JsonResponse({'movies': serializer.data})

def giveMovieInfo(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(instance=movie)
    result = serializer.data
    result['snapshot_url'] = []
    
    for snapshot in serializer.data['snapshot_url'].split(', '):
        if 'https://ssl.pstatic.net/static/movie/2012/06/adult_img74x74.png' == snapshot:
            continue
        result['snapshot_url'].append(snapshot)
    reviews = result['reviews']
    reviews = [{'id': review['id'], 'user_id': review['user'],'username': get_object_or_404(User, pk=review['user']).username,'score': review['score'], 'content': review['content']} for review in reviews]
    result['reviews'] = reviews
    result['liked_users_info'] = []
    pprint(result)
    for liked_user in result['liked_users']:
        liked_user = get_object_or_404(User, pk=liked_user)
        serializer = UserSerializer(instance=liked_user)
        result['liked_users_info'].append(serializer.data)
<<<<<<< HEAD
    
=======
>>>>>>> 2769211eefc8eb0d9aa4191484f7d7cfca148db6
    return JsonResponse(result)

def giveActorInfo(request, actor_id):
    
    actor = get_object_or_404(Actor, pk=actor_id)
    serializer = ActorSerializer(instance=actor)
    movie_list = []
    for movie_id in serializer.data['movies']:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie_serializer = MovieSerializer(instance=movie)
        movie_list.append(movie_serializer.data)

    result = serializer.data
    result['movies'] = movie_list
    return JsonResponse(result)

def giveDirectorInfo(request, director_id):
    
    director = get_object_or_404(Director, pk=director_id)
    serializer = DirectorSerializer(instance=director)
    movie_list = []
    for movie_id in serializer.data['movies']:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie_serializer = MovieSerializer(instance=movie)
        movie_list.append(movie_serializer.data)

    result = serializer.data
    result['movies'] = movie_list
    return JsonResponse(result)

def movieForUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    result = {
        'actors': [],
        'directors': [],
        'users': []
    }
    for actor in user.like_actors.all():
        for movie in actor.movies.all():
            if movie in user.like_movies.all():
                continue
            serializer = MovieSerializer(instance=movie)
            if serializer.data in result['actors']:
                continue
            result['actors'].append(serializer.data)

    for director in user.like_directors.all():
        for movie in director.movies.all():
            serializer = MovieSerializer(instance=movie)
            if serializer.data in result['directors']:
                continue
            result['directors'].append(serializer.data)

    for like_movie in user.like_movies.all():
        for aside_user in like_movie.liked_users.all():
            for movie in aside_user.like_movies.all():
                if movie in user.like_movies.all():
                    continue
                serializer = MovieSerializer(instance=movie)
                if serializer.data in result['users']:
                    continue
                result['users'].append(serializer.data)

    return JsonResponse(result)

@api_view(['POST'])
def createRecommend(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    creation_form  = request.data
    movies = creation_form['movies']
    temp_recommend = Recommend()
    temp_recommend.title = creation_form['title']
    temp_recommend.user = user
    temp_recommend.discription = creation_form['discription']
    temp_recommend.save()
    for movie in movies:

        movie_id = movie['movie']['id']
        add_movie = get_object_or_404(Movie, pk=movie_id)

        add_moviecomment = movie['movieComment']
        temp_movieComment = MovieComment()
        temp_movieComment.content = add_moviecomment
        temp_movieComment.recommend = temp_recommend
        temp_movieComment.movie = add_movie
        temp_movieComment.save()
        temp_recommend.movies.add(add_movie)
    return JsonResponse({})

@api_view(['POST'])
def deleteRecommend(reqeust, recommend_id):
    recommend = get_object_or_404(Recommend, pk=recommend_id)
    recommend.delete()
    return Response(status=204)

@api_view(['POST'])
def createMovieReview(request, user_id, movie_id):
    form = ReviewCreationForm(request.data)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = user_id
        comment.movie_id = movie_id
        comment.save()

        context = {
            'id': comment.id,
            'user': user_id,
            'username': get_object_or_404(User, pk=user_id).username,
            'content': comment.content,
            'score': comment.score,
        }
        return JsonResponse(context)
    return JsonResponse(form.data)

@api_view(['POST'])
def deleteRevieReview(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return Response(status=204)

@api_view(['POST'])
def createRecommendReview(request, user_id, recommend_id):
    form = RecommendReviewCreationForm(request.data)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = user_id
        comment.recommend_id = recommend_id
        comment.save()

        context = {
            'id': comment.id,
            'user': user_id,
            'username': get_object_or_404(User, pk=user_id).username,
            'content': comment.content,
        }
        return JsonResponse(context)
    return JsonResponse(form.data)
    
@api_view(['POST'])
def deleteRecommendReview(request, review_id):
    review = get_object_or_404(RecommendReview, pk=review_id)
    review.delete()
    return Response(status=204)

def recommendList(request, user_id):
    if not user_id:
        recommends = Recommend.objects.all()
    else:
        user = get_object_or_404(User, pk=user_id)
        recommends = Recommend.objects.filter(user=user)
    
    serializer = RecommendSerializer(instance=recommends, many=True)

    return JsonResponse({'recommends': serializer.data})
    
def giveUserDetail(reqeust, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(instance=user)

    return JsonResponse(serializer.data)

def recommendDetail(request, recommend_id):
    recommend = get_object_or_404(Recommend, pk=recommend_id)
    serializer = RecommendSerializer(instance=recommend)

    result = serializer.data
    
    reviews = result['recommend_reviews']
    reviews = [{'id': review['id'], 'user_id': review['user'],'username': get_object_or_404(User, pk=review['user']).username, 'content': review['content']} for review in reviews]
    result['recommend_reviews'] = reviews
    

    return JsonResponse(result)


@api_view(['POST'])
def likemovie(request, movie_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    movie = get_object_or_404(Movie, pk=movie_id)

    if movie.liked_users.filter(pk=user.id).exists():
        user.like_movies.remove(movie)
        liked = False
    else:
        user.like_movies.add(movie)
        liked = True
    context = {'liked': liked, 'count': movie.liked_users.count()}
    return JsonResponse(context)


@api_view(['POST'])
def likedirector(request, director_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    director = get_object_or_404(Director, pk=director_id)

    if director.liked_users.filter(pk=user.id).exists():
        user.like_directors.remove(director)
        liked = False
    else:
        user.like_directors.add(director)
        liked = True
    context = {'liked': liked, 'count': director.liked_users.count()}
    return JsonResponse(context)


@api_view(['POST'])
def likeactor(request, actor_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    actor = get_object_or_404(Actor, pk=actor_id)

    if actor.liked_users.filter(pk=user.id).exists():
        user.like_actors.remove(actor)
        liked = False
    else:
        user.like_actors.add(actor)
        liked = True
    context = {'liked': liked, 'count': actor.liked_users.count()}
    return JsonResponse(context)


@api_view(['POST'])
def likerecommend(request, recommend_id, user_id):
    user = get_object_or_404(User, pk=user_id)
    recommend = get_object_or_404(Recommend, pk=recommend_id)

    if recommend.liked_users.filter(pk=user.id).exists():
        user.like_recommends.remove(recommend)
        liked = False
    else:
        user.like_recommends.add(recommend)
        liked = True
    context = {'liked': liked, 'count': recommend.liked_users.count()}
    return JsonResponse(context)
