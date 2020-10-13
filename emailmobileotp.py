from flask import *
from twilio.rest import Client
import random

app = Flask(__name__, template_folder='template')
otp=random.randrange(000000,999999)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def getotp():
    number = request.form['number']
    val = otpapi(number)
    if val:
        return  render_template('verify.html')

def otpapi(number):
    account_sid = "AC65bb455ea7a7f61cd41bd44ea8ebf6b0"
    account_token = "5edb697c843f8356ebad03c9089c78ca"
    client = Client(account_sid,account_token)
    body = "your otp is" + str(otp)
    message = client.messages.create(
        body=body,
        from_ = '+19285698961',
        to = number
    )
    if message.sid:
        return True
    else:
        False
@app.route('/success', methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return "<h3>Mobile OTP varification succesfull</h3>"
    return "<h3>Please Try Again</h3>"

if __name__ == '__main__':
    app.run(debug=True)