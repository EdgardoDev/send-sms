from dotenv import load_dotenv
import os 
from twilio.rest import Client

load_dotenv() 

account_sid = os.getenv("ACCOUNT_SID") 
auth_token = os.getenv("AUTH_TOKEN")  
my_phone_number = os.getenv("MY_PHONE_NUMBER")
client = Client(account_sid, auth_token)

message = client.messages.create(  
                              messaging_service_sid='MGf249a4eb22ba71bb71aab264494d84c5', 
                              body='Hello from Python Code!',      
                              to=my_phone_number 
                          ) 

print(message.sid)