# djangorestframeworkapiでエンドポイントの作成

## 仮想環境の作成

```bash
python3 -m venv venv
```

## 仮想環境のActivate と deactidate

activate

```bash
source venv/bin/activate
```

deactivate

```bash
deactivate
```

## requirements.txtから必要なモジュールをインストールする

```bash
pip install -r requirements.txt
```

## requirements.txtをファイルに出力

```bash
pip freeze > requirements.txt
```

## djangoの作成

プロジェクトの作成

```bash
django-admin startproject rest_api .
```

アプリケーションの作成

```bash
django-admin startapp api
```

起動確認

```bash
python manage.py runserver
```

## rest_apiのsetting.pyの編集

追加でインポート

```bash
from datetime import timedelta
from decouple import config
from dj_database_url import parse as dburl
```

SECRET_KEYとDEBUGを.envを作成し、記述。

```bash
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
```

INSTALLED_APPSを追加

```bash
'rest_framework',
'api.apps.ApiConfig',
'corsheaders',
'djoser',
```

MIDDLEWAREを追加

```bash
'corsheaders.middleware.CorsMiddleware',
```

CORS_WHITELISTの追加

```bash
CORS_WHITELIST = [
    "http://localhost:3000",
]
```

SIMPLE_JWTの追加

```bash
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES" : ('JWT',),
    "ACCESS_TOKEN_LIFETIME" : timedelta(minutes=60),
}
```

REST_TRAMEWORKの追加

```bash
REST_TRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES" : [
        'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES" : [
        'rest_framework.simplejwt.authntication.JWTAuthentication',
    ],
}
```

DATABASEの変更

```bash
default_dburl = 'sqlite:///' + str(BASE_DIR / "db.sqlite3")
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}
```

言語と時間設定

```bash
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

言語と時間設定

```bash
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

herokuデプロイ用.

```bash
STSTIC_ROOT=str(BASE_DIR / 'staticfiles')
```
