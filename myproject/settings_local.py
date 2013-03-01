# Local settings
import os

# OAuth keys for Social Auth

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_API_SECRET = os.environ['FACEBOOK_API_SECRET']
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
FOURSQUARE_CONSUMER_KEY = ''
FOURSQUARE_CONSUMER_SECRET = ''
VK_APP_ID = ''
VK_API_SECRET = ''
LIVE_CLIENT_ID = ''
LIVE_CLIENT_SECRET = ''
SKYROCK_CONSUMER_KEY = ''
SKYROCK_CONSUMER_SECRET = ''
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''

GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'access_type': 'offline'}
GOOGLE_EXTRA_DATA = [('oauth_token', 'oauth_token')]
GOOGLE_SREG_EXTRA_DATA = [('oauth_token', 'oauth_token')]
GOOGLE_AX_EXTRA_DATA = [('oauth_token', 'oauth_token')]

AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET']
