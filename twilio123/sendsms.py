from twilio.rest import Client
from twilio_app import account_sid, auth_token , my_cell , my_twilio

client = Client(account_sid, auth_token)

my_msg="".join([ "me nub\n" for i in range(100)])

message=client.messages.create(to=my_cell , from_=my_twilio , body=my_msg)
