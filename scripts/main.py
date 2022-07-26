import os
from twilio.rest import Client

"""
The goal of this project is to create a program that will send mass text
messages during an emergency. This will leverage the Twilio API to send 
a text to a group of users.
"""
account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
auth_token = os.environ['TWILIO_AUTH_TOKEN'] 

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body = 'Hello Ben.\
              This is a test of our emergency notification system.\
              Please disregard this message.',
        from_ = '############', #These will need to be replaced with an acutal value
        to = '###########'
    )

print(message.sid)

