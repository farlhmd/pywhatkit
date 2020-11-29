from twilio.rest import Client

account_sid = 'your_acc_sid'
auth_token = 'yout_auth_token'
client = Client( account_sid, auth_token )

def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='this is the text',
        to='whatsapp:+to'
    )

    print( message.sid )
