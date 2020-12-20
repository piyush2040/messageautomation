from twilio.rest import Client 
 
account_sid = 'AC16a07c5402ec1fc72177c2de1f17f8fa' 
auth_token = '7471d1196f3f77f81e8da28b0180fc59' 
client = Client(account_sid, auth_token) 
def send_message(): 
    message = client.messages.create( 
                                from_='+12517583965',  
                                body='hello',      
                                to='+916299650293' 
                            ) 
 
    print(message.sid)