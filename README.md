Base Project

On command line run the following: { make sure to replace xxxx with the actual values you get from AWS website }

heroku config:add S3_KEY=xxxx
heroku config:add S3_SECRET=xxxx

export S3_KEY=xxxx
export S3_SECRET=xxxx


==Start up steps==

1) git clone
2) heroku create
3) git push heroku master



== Trouble shooting ==

=== View logs===
heroku logs

heroku ps