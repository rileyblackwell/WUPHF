import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from comms.channels import WUPHF

class ContactInfo(object):
    def __init__(self, TWILIO_PHONE_NUMBER, RECEIPIENT_NUMBER, SENDER_EMAIL, RECEIPIENT_EMAIL, message):
        self.TWILIO_PHONE_NUMBER = TWILIO_PHONE_NUMBER
        self.RECEIPIENT_NUMBER = RECEIPIENT_NUMBER
        self.SENDER_EMAIL = SENDER_EMAIL
        self.RECEIPIENT_EMAIL = RECEIPIENT_EMAIL
        self.message = message

    def get_twilio_number(self):
        return self.TWILIO_PHONE_NUMBER
    
    def get_receipient_number(self):
        return self.RECEIPIENT_NUMBER
    
    def get_sender_email(self):
        return self.SENDER_EMAIL
    
    def get_receipient_email(self):
        return self.RECEIPIENT_EMAIL

    def get_message(self):
        return self.message


def setup():
    print('Enter your text message:')
    message = input()

    print('Enter the phone number that you are sending to:')
    RECEIPIENT_NUMBER = input()

    print('Enter the email address that you are sending to:')
    RECEIPIENT_EMAIL = input()
    
    
    twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    
    sg_client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))

    contactinfo = ContactInfo(os.getenv('TWILIO_PHONE_NUMBER'), RECEIPIENT_NUMBER, os.getenv('SENDER_EMAIL'), RECEIPIENT_EMAIL, message)
    
    wuphf = WUPHF(twilio_client, sg_client, Mail, contactinfo)

    return wuphf