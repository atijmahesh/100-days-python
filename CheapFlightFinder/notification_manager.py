from twilio.rest import Client
import os
# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACC_SID'], os.environ["AUTH_TOKEN"])

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:14155238886',
            body=message_body,
            to=f'whatsapp:+14086181185'
        )
        print(message.sid)