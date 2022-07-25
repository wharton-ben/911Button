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

number = client.pricing.v2.voice.numbers('###############').fetch()

print(number.outbound_call_prices)
