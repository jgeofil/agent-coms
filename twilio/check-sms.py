from twilio.rest import Client
import os
import dotenv


dotenv.load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

verification = client.verify.v2.services(
    "VA8d02835d6c30c688e547a24262de89a5"
).verifications.create(to="+15818491348", channel="sms")

print(verification.sid)
