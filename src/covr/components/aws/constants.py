from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "DUMMY-ACCESS-KEY-ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "DUMMY-SECRET-ACCESS-KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", "covr")
ENDPOINT_URL = os.getenv("ENDPOINT_URL", "DUMMY-ENDPOINT-URL")
