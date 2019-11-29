# Movie_Recommendation

### 1. 팀원 정보 및 업무 분담 내용

- 김은성 : open API, 크롤링을 통한 DB생성, Movie, Actor, Director, Recommend 등 다양한기능 구현

  ​		      https://github.com/unsung107

- 윤가영 : open API를 통한 DB생성, 회원가입, 로그인 / 회원가입 / 로그아웃, 좋아요 등 기능 구현, CSS

  ​			 https://github.com/GaYoung87

  

### 2. 데이터베이스 모델링(ERD)

![image](https://user-images.githubusercontent.com/52685278/69401360-3d89eb80-0d38-11ea-9142-398bc0985974.png)



### 3. 목표 서비스 구현 및 실제 구현 정도

```bash
# Django
$ pip install django
$ python -m pip install --upgrade pip
$ pip install djangorestframework
$ pip install python-decouple
$ pip install request
$ pip install bs4
$ pip install requests
$ pip install django-cors-headers
$ pip install djangorestframework-jwt
$ pip install Pillow

# Vue
$ npm init
$ npm install
$ npm install axios
$ npm install --save date
$ npm install jwt-decode
```

#### 11월 21일(목)

- 기능 구상 + 모델 구성

#### 11월 22일(금)

- OPEN API + 네이버 크롤링으로 db 생성
- login / 회원가입 생성

#### 11월 25일(월)

- 회원가입 / 로그아웃 기능 구현
- Movie, Actor, Director, Recommend + 관련 Detail 기능 구현

#### 11월 26일(화)

- Mypage, Movie / Actor / Recommend 세부기능 구현 (modal, tooltips)
- DB 수정, model 수정

#### 11월 27일(수)

- 좋아요, 댓글 기능 구현
- CSS로 홈페이지 꾸미기

#### 11월 28일(목)

- CSS로 꾸미기

- 기능 수정하며 제대로 작동되는지 확인

  

### 4. 핵심기능

- 장르 별로 영화 보여주기

- Movie Detail 보여주기(title, discription, director, actor, vedio, snapshot, reveiw)

- 감독 및 배우가 나온 영화 보여주기

- 영화, 감독, 배우에 대한 좋아요를 통해 나와 같은 영화를 좋아요 한 사람의 영화들도 보여주기

- 추천 리스트 작성 및 보여주기

- Movie For You : 내가 좋아하는 배우 / 감독 나오는 영화, 내가 좋아한 영화를 좋아하는 유저들이 좋아하는 영화

  

### 5. 배포 서버URL

https://geeg-3b5d2.firebaseapp.com](https://geeg-3b5d2.firebaseapp.com/