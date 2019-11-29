# Vue사용해 웹 제작 후 FireBase로 배포하기

## Vue

1. 프로젝트 생성하기
2. 생성 후 hosting: 정적인 웹사이트 배포

```bash
$ npm install -g firebase-tools
$ firebase login  # y
```

3. hosting서비스 사용을 위해 설정

```bash
student@M702 MINGW64 ~/development/MovieRecommeds/pjt-front (master)
$ firebase init
# ( ) Database: Deploy Firebase Realtime Database Rules
# ( ) Firestore: Deploy rules and create indexes for Firestore
# ( ) Functions: Configure and deploy Cloud Functions
#>(*) Hosting: Configure and deploy Firebase Hosting sites
# ( ) Storage: Deploy Cloud Storage security rules
# ( ) Emulators: Set up local emulators for Firebase features

# Use an existing project
? What do you want to use as your public directory? dist

$ npm run build
$ firebase deploy
```



## DRF

1. 과정

```bash
student@M702 MINGW64 ~/development/MovieRecommeds/pjt-back (master)
$ python manage.py dumpdata accounts.User > users.json
# user.json이라는 파일 생김 -> accounts파일 안에 fixtures파일 생성 후 넣기!
# db삭제하기 -> 배포 후 추가
$ python manage.py loaddata users.json
```

```python
# settings에 
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['*']  # 모두 접근 가능
```

