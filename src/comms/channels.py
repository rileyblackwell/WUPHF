class WUPHF(object):
    """Utilize Twilio's Messaging and Voice API's in def send_message and def make_call.
        def create_WUPHF is all that needs to be called from the main program to send a WUPHF.
    """
    def __init__(self, twilio_client, sg_client, Mail, contactinfo):
        self.client = twilio_client
        self.sg_client = sg_client
        self.Mail = Mail
        self.TWILIO_PHONE_NUMBER = str(contactinfo.get_twilio_number())
        self.RECEIPIENT_NUMBER = str(contactinfo.get_receipient_number())
        self.SENDER_EMAIL = str(contactinfo.get_sender_email())
        self.RECEIPIENT_EMAIL = str(contactinfo.get_receipient_email())
        self.message = str(contactinfo.get_message())


    def send_message(self):         
        msg = self.client.messages.create(
            to=self.RECEIPIENT_NUMBER,
            from_=self.TWILIO_PHONE_NUMBER,
            body=self.message
        )

    def make_call(self):
        call = self.client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=self.RECEIPIENT_NUMBER,
            from_=self.TWILIO_PHONE_NUMBER
        )
    def send_email(self):
        email = self.Mail(
            from_email='rileyblackwell5@gmail.com',
            to_emails='rileyblackwel@gmail.com',
            subject='Testing out Sendgrid',
            html_content=self.message)
        try:
            self.sg_client
            response = self.sg_client.send(email)
            # statsus code 202 if program sucedes
            print(response.status_code)
    
        except Exception as e:
            print(e.message)

    def create_WUPHF(self):
        self.send_email()
        self.send_message()
        self.make_call()
        



