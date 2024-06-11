# account_sid = 'ACcc386e6626e6a636acc4e1c939d04949'
# auth_token = 'a5e199ba227d53f7da5bf7beb118a580'
# twilio_from_number = '+12097200667'


# sensor_data1/twilio_credentials.py

import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_FROM_NUMBER = os.getenv('TWILIO_FROM_NUMBER')

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_FROM_NUMBER:
    raise ValueError("Twilio credentials not found in environment variables")
