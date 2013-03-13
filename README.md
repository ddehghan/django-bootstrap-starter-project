
Base Django Template Project
============================

What is included?
-----------------
* Meant for deploying to Heroku
* Social Auth. (Facebook, Google, Yahoo) Oauth


What you need to get started?
-----------------------------

### Mininmum requirements

* Sign up for AWS account
* Get AWS keys AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


### Advance requirements

* Facebook Oauth keys: FACEBOOK_APP_ID, FACEBOOK_API_SECRET
* Google OAuth keys: GOOGLE_OAUTH2_CLIENT_ID, GOOGLE_OAUTH2_CLIENT_SECRET



Setup Steps
===========
* git clone
* heroku create
* git push heroku master
* On command line run the following: { make sure to replace xxxx with the actual values you get from AWS website }

> bash myproject/settings_local.heroku.sh

> source myproject/settings_local.env.sh

* Check settings

> heroku config

> printenv



Helpful Commands
================



### View logs and status
> heroku logs

> heroku ps

> heroku config


### Heroku 
Deployment of Django on Heroku https://devcenter.heroku.com/articles/django

> heroku run python manage.py syncdb

> heroku run python manage.py migrate website


> heroku domains:add www.example.com


> python manage.py collectstatic --noinput;

> heroku config:add DISABLE_COLLECTSTATIC=1         # To disable static collection
> heroku config:remove DISABLE_COLLECTSTATIC

> heroku pg:reset DATABASE

> git push heroku drawthefuture:master