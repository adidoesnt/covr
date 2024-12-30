from dotenv import load_dotenv
import os

load_dotenv()

RESUME_QUEUE_URL = os.getenv("RESUME_QUEUE_URL", "DUMMY-QUEUE-URL")
POLLING_INTERVAL_MS = os.getenv("POLLING_INTERVAL_MS", "10000")