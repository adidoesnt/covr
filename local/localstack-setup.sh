#!/bin/sh
echo "Initializing localstack sqs..."

awslocal sqs create-queue --queue-name resume-queue --profile covr --region ap-southeast-1 >> /dev/null

echo "localstack sqs initialized."

exit 0