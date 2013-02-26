Base Project

On command line run the following: { make sure to replace xxxx with the actual values you get from AWS website }

bash myproject/settings_local.heroku.sh
source myproject/settings_local.env.sh

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


https://devcenter.heroku.com/articles/django