import os
from flask import Flask
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/')

def index():
	message = client.messages.create(
		to="+15109539491",
		from_="+19096751502",
		body="Motion detected at - date time")
	return(message.sid)
if __name__ == "__main__":
	app.run()