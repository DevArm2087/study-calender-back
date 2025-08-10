from pathlib import Path
from datetime import timedelta
import os
import dj_database_url

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید امنیتی (در محیط توسعه می‌تونی همین رو بزاری، ولی در سرور باید از ENV بگیری)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

# حالت دیباگ (True برای لوکال، False برای آنلاین)
DEBUG = os.environ.get("DEBUG", "True") == "True"

# دامنه‌ها و هاست‌های مجاز
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# اپلیکیشن‌های نصب‌شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',                     # برای CORS
    'rest_framework',
    'accounts',
    'rest_framework_simplejwt',
]

# میان‌افزارها (Middleware)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # باید در بالا باشه
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# مسیر فایل‌های URL
ROOT_URLCONF = 'myproject.urls'

# قالب‌ها (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'myproject.wsgi.application'

# تنظیمات دیتابیس (SQLite در لوکال، DATABASE_URL در سرور)
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# قوانین رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# زبان و زمان
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# کلید پیش‌فرض برای مدل‌ها
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ["study-calender-back.onrender.com", "localhost"]


# تنظیمات CORS
CORS_ALLOWED_ORIGINS = os.environ.get(
    "CORS_ALLOWED_ORIGINS",
    "http://localhost:5173, " \
    "https://study-calender-front.onrender.com"
).split(",")


# تنظیمات DRF و JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
