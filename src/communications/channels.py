class WUPHF(object):
    def __init__(self, client, TWILIO_PHONE_NUMBER, receipient, message):
        self.client = client
        self.TWILIO_PHONE_NUMBER = str(TWILIO_PHONE_NUMBER)
        self.receipient = str(receipient)
        self.message = str(message)
        
    def send_message(self):         
        msg = self.client.messages.create(
            to=self.receipient,
            from_=self.TWILIO_PHONE_NUMBER,
            body=self.message
        )

    def make_call(self):
        call = self.client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=self.receipient,
            from_=self.TWILIO_PHONE_NUMBER
        )

    
    def create_WUPHF(self):
        self.send_message()
        self.make_call()



