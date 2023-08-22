# 아두이노 서버 🤖

안녕하세요! 아두이노 서버입니다. 아두이노에서 데이터를 받아서 서버에 저장하고, 웹사이트에서 그 데이터를 볼 수 있어요!

## 주요 기능 🚀
1. **아두이노 데이터 수신**: 아두이노에서 보내준 데이터를 서버에서 받을 수 있어요.
2. **데이터 저장**: 받은 데이터는 서버에 안전하게 저장됩니다.
3. **웹사이트 조회**: 저장된 데이터를 웹사이트에서 간단하게 확인할 수 있습니다.

## 코드 설명 📜
- `models.py`에서는 데이터의 형식을 정의하고 있어요. 어떤 데이터를 어떻게 저장할지를 결정합니다.
- `GatherItemView`는 아두이노에서 보내준 데이터를 전달받는 부분입니다. 데이터가 오면 잘 저장해줄게요!
- `admin`에서는 저장된 데이터를 웹사이트로 볼 수 있습니다. 데이터를 확인하고 싶을 때 여기서 볼 수 있어요!

## 서버 실행 방법 🏃‍♂️
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver 0.0.0.0:8000

---


궁금한 점이 있으면 언제든지 알려주세요! 🌟