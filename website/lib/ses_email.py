from boto.ses.connection import SESConnection
from myproject.settings_local import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def send_email(subject, body):
    source = "ddehghan@gmail.com"
    to_addresses = ["ddehghan@gmail.com"]
    connection = SESConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                               aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    connection.send_email(source, subject, body, to_addresses)