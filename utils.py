import requests
from django.conf import settings 

def send_otp(mobile, otp):

    url = f"https://www.twilio.com/docs/iam/keys/api-key(settings.SMS_API_KEY)/SMS/{mobile}/{otp}/Seu OTP é"
    payload = ""
    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = requests.get(url, data=payload, headers=headers)

    return bool(response.ok)