import boto3
import time
import json

from covr.components.resume_parser.constants import RESUME_QUEUE_URL, POLLING_INTERVAL_MS
from covr.components.aws.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_PROFILE, ENDPOINT_URL

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
    profile_name=AWS_PROFILE,
)

sqs = session.client(
    service_name='sqs',
    endpoint_url=ENDPOINT_URL,   
)

def delete_message(receipt_handle):
    sqs.delete_message(QueueUrl=RESUME_QUEUE_URL, ReceiptHandle=receipt_handle)
    
def pull_message():
    response = sqs.receive_message(QueueUrl=RESUME_QUEUE_URL, MaxNumberOfMessages=1)
    
    if "Messages" not in response:
        print("No messages found.")
        return
    
    message = response["Messages"][0]
    
    print(f"Message received: {message['Body']}")
    
    receipt_handle = message["ReceiptHandle"]
    
    print(f"Deleting message with receipt handle: {receipt_handle}")
    delete_message(receipt_handle)
    
def pull_messages():
    interval = int(POLLING_INTERVAL_MS) / 1000
   
    while True:
        pull_message()
        time.sleep(interval)
        