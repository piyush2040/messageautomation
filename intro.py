from twilio.rest import Client 
#account_sid and auth_token is changed for security purposes. 
account_sid = '###############################' 
auth_token = '###############################' 
client = Client(account_sid, auth_token) 
def send_message(): 
    message = client.messages.create( 
                                from_='+12517583965',  
                                body='This is the message that you want to send',      
                                to='##############' 
                            ) 
 
    print(message.sid)
