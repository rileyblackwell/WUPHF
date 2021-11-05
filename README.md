# Create a WUPHF!

# Create a simultanous text message, email, and phone call with wuphf.py.

## Requires python 3, the twilio python helper library, and sendgrid helper library.

## Create your virtual environment (pipenv recommended).
pipenv shell

## Use pip or pipenv to install the twilio and sendgrid packages and their subdependiences.

pipenv install twilio.
pipenv install sendgrid.

## Add your Twilio creditials to a .env file

Create a .env file and add your Twilio creditials as the environment variables TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
Also add your email as the environment variable SENDER_EMAIL

e.g. TWILIO_PHONE_NUMBER = '+1237891234'

## Add your Sengrid API Key to a sendgrid.env file

Create a sendgrid.env file and add your API Key for export.

e.g. export SENDGRID_API_KEY= 'YOUR API KEY'


# Create a WUPHF!

In the main WUPHF directory type: source ./sendgrid.env

Next navigate to the src folder and type: python wuphf.py.

The terminal will then promept you to the enter the message that you wish to send and the phone number and email that you are sending it to.
A phone call will also begin.

Congratulations you just sent a WUPHF!

 
