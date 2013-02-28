Base Project

=Sign up for AWS=

==What you need to get started==

FACEBOOK_APP_ID
FACEBOOK_API_SECRET


GOOGLE_OAUTH2_CLIENT_ID
GOOGLE_OAUTH2_CLIENT_SECRET


AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY




On command line run the following: { make sure to replace xxxx with the actual values you get from AWS website }

bash myproject/settings_local.heroku.sh
source myproject/settings_local.env.sh

==check settings==

heroku config
printenv


==Start up steps==

1) git clone
2) heroku create
3) git push heroku master



== Trouble shooting ==

=== View logs===
heroku logs

heroku ps

heroku run python manage.py syncdb


heroku domains:add www.example.com

heroku config

python manage.py collectstatic --noinput;

# disable static collection
heroku config:add DISABLE_COLLECTSTATIC=1

https://devcenter.heroku.com/articles/django


heroku pg:reset DATABASE