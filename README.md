### DRF with unit Testing
- <b>Simple Django Rest Framework (DRF) With Django Unit Testing Performs.</b>

- #### Functionality
- Signup
- Login 
- Account Activation Mail
- Logout 
- Change Passord
- Forget password
- User Details
- Check Authentication
- CSRF Protection for secure user data transmission.
- Unit Testing
- Coverage

- #### Make sure you have the following installed:

- Python (>=3.6)
- Django
- Django Rest Framework
- Dependencies (requirements.txt)

#### Steps that need to follow

- #### Installation Django REST framework 

- Documentation [link](https://www.django-rest-framework.org/)  

- Installation

```bash
pip install djangorestframework
```

- Add 'rest_framework' to your INSTALLED_APPS setting.

```bash
INSTALLED_APPS = [
    'rest_framework',
]
```

- Add the following to your root urls.py file.

```bash
urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
```

- #### Install Cross-origin resource sharing (CORS)

```bash
Documentation [link](https://pypi.org/project/django-cors-headers/)

pip install django-cors-headers

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

you connect you backed to forntend on error comes (cors policy error)
so that we have to install 
```

- then add it to your installed apps

```bash
INSTALLED_APPS = [
    "corsheaders",
]
```

- You will also need to add a middleware class to listen in on responses.

```bash
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]
```

- #### Installation dotenv

```bash
Documentation [link](https://pypi.org/project/python-dotenv/)

dotenv : when working on a django project, we have some secret keys, OAuth keys and other critical information that needs to be kept safe and private. By no means should you expose such kind of keys because it makes your system vulnerable to security attacks.

pip install python-dotenv
```

- #### setup and Installation mysql

```bash
Documentation [link](https://pypi.org/project/mysqlclient/)

pip install mysqlclient
```

- Configure the middleware’s behaviour in your Django settings. You must set at least one of three following settings:

```bash
CORS_ALLOWED_ORIGINS
CORS_ALLOWED_ORIGIN_REGEXES
CORS_ALLOW_ALL_ORIGINS

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

- #### setup mysql in setting file 

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

- #### Email Configuration

```bash
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_USE_TLS = True
```

- #### Django rest framework configration 

```bash
REST_FRAMEWORK = {
    # Enable Session Authentication for App
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    # Enable IsAuthenticated Permission
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Disable Browsable API and Render JSON
    # 'DEFAULT_RENDERER_CLASSES':('rest_framework.renderers.JSONRenderer',),
}
```

- #### Set session cookies expaire time 

```bash
Sessionid cookies Expire default is 1209600 sec = 14 days
SESSION_COOKIE_AGE = 1800   # 30 Min
```

- #### Serializers

```bash
The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.
```

- #### Authentication

- To register a new user, use the /api/signup/ endpoint.
- After registration, an activation email will be sent to your email address. Follow the link to activate your account.
- Log in using the /api/login/ endpoint.
- Use the /api/logout/ endpoint to log out.

- #### Api Endpoints

- CSRF Token : /api/account/csrf_cookie/
- Registration: /api/account/registration/
- Activation: /api/account/activate/<str:uid>/<str:token>/
- Confirm activation: /api/account/activate/
- Login: /api/account/login/
- Logout: /api/account/logout/
- User Details: /api/account/user/
- Password Change: /api/account/change_password/
- delete Account: /api/account/delete/
- Reset password with email: /api/account/reset_password/
- reset Password token: /api/account/reset_password/<str:uid>/<str:token>/
- confirm rest password: /api/account/reset_password_confirm/
- Check Authentication: /api/account/checkauth/

- #### make migration and migrate command 
```bash
python manage.py makemigration 

python manage.py migrate
```

- #### Create Super user 
```bash
python manage.py createsuperuser
```

- #### Unit Testing 

```bash
Django rest framework(DRF) unit testing documentation [link](https://www.django-rest-framework.org/api-guide/testing/)

Django test Case Writing [link](https://docs.djangoproject.com/en/4.2/topics/testing/overview/)

```
- #### Unit Testing Structure

```bash
Structure your tests to fit your Project. I tend to favor putting all tests for each app in the tests.py file and grouping tests by what I’m testing - e.g., models, views, forms, etc.

You can also bypass (delete) the tests.py file altogether and structure your tests in this manner within each app:

└── app_name
    └── tests
        ├── __init__.py
        ├── test_serializers.py
        ├── test_models.py
        └── test_views.py
```
- #### Importan point 

```bash
 if you create custome test class then you have to delete by default genereted tests.py class 
```

- #### Use Coverage in testing

```bash
Code coverage describes how much source code has been tested. It shows which parts of your code are being exercised by tests and which are not. It’s an important part of testing applications, so it’s strongly recommended to check the coverage of your tests.

Documentation [link](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/), [link2](https://coverage.readthedocs.io/en/7.3.2/)

pip install coverage
```

- #### Run Unit testing file
```bash
coverage run --source='.' manage.py test myapp
or 
coverage run --source='authAccount' manage.py test
```
- run this for create testing report

```bash
coverage report
```
- #### some packeage that can use in testing 

- Faker

```bash
Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

pip install Faker

Example :- 

for _ in range(10):
  print(fake.name())
```