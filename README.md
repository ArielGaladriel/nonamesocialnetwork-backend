<h2 align="center">Backend for social network [working title]</h2>

This is a backend for a social network (SN) [working title]. 
Concept of this SN will be added after product release.

**Stack:**
- Python 3.10.5
- Django 4.1
- DRF 3.13.1
- Postgres 14

**Current version - alpha 0.0.1 - have the following functionality:**
- Creation of user's profile, adding and editing additional information about themselves
- Authentication via JWT or OAuth 2.0 (Google) 
- User's activation confirmation (via email), password reset and 
other basic actions of authentication system are provided by Djoser library
- For user's profile and posts the following permission options are provided: 'public', 
'followers only' and 'private'
- User can create, edit and delete their posts. Other users can view them
depending on privacy settings of every post. 
- User can subscribe/unsubscribe for other users and delete their followers.
If subscribed profile is not public, it's owner should confirm subscription request.
- User can view list of their followers/followee
- User can view other user's profiles depending on their privacy settings

You can view API documentation made by swagger (see below).

### Getting started
##### 1) Clone this repository
    git clone <link>
##### 2) Create .env.dev in the root of the project 
    SECRET_KEY=django-insecure-9$1^0rdh84p_=os-!b@eyw8*ms)71pepte*--#i%_4+y95*=y+
    DEBUG=1
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=socialnetwork
    POSTGRES_USER=socialnetworkuser
    POSTGRES_PASSWORD=12345
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    DATABASE=postgres

    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=yourmail@gmail.com
    EMAIL_HOST_PASSWORD=*********
    EMAIL_USE_TLS=True
    EMAIL_PORT=587

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=*********
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=*********
    SOCIAL_AUTH_RAISE_EXCEPTIONS=False
    SOCIAL_AUTH_JSONFIELD_ENABLED=True
##### 3) Create an image
    docker-compose build
##### 4) Run container
    docker-compose up
##### 5) Make migrations
    docker exec -it <CONTAINER NAME> python manage.py makemigrations
    docker exec -it <CONTAINER NAME> python manage.py migrate
##### 6) Create superuser
    docker exec -it <CONTAINER NAME> python manage.py createsuperuser
##### 7) Visit next link to view API
    http://127.0.0.1:8000/swagger/
