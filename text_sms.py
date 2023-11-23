import Keys
from twilio.rest import Client
to='+91*****56'

def send_text(body):
    client = Client(Keys.AccountSID, Keys.AccountToken)
    message = client.messages.create(body=body, from_=Keys.Phno, to=to)
    print(message.body)
