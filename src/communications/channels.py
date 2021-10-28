class WUPHF(object):
    """Utilize Twilio's Messaging and Voice API's in def send_message and def make_call.
        def create_WUPHF is all that needs to be called from the main program to send a WUPHF.
    """
    def __init__(self, client, TWILIO_PHONE_NUMBER, RECEIPIENT_NUMBER, message):
        self.client = client
        self.TWILIO_PHONE_NUMBER = str(TWILIO_PHONE_NUMBER)
        self.RECEIPIENT_NUMBER = str(RECEIPIENT_NUMBER)
        self.message = str(message)
        
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

    
    def create_WUPHF(self):
        self.send_message()
        self.make_call()



