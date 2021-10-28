import os
from twilio.rest import Client
from communications.channels import WUPHF

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER') 
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
RECEIPIENT_NUMBER = os.getenv('RECEIPIENT_NUMBER')

print('Enter your text message')
message = input()

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

wuphf = WUPHF(client, TWILIO_PHONE_NUMBER, RECEIPIENT_NUMBER, message)

wuphf.create_WUPHF()