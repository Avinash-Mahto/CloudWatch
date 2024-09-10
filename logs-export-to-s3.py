import boto3
import gzip
import json
import base64
import time

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Define your S3 bucket name
    s3_bucket = 'BUCKET_NAME'  # Replace with your actual S3 bucket name
    
    # Define the EC2 instance ID (you have only one EC2 instance)
    instance_id = 'INSTANCE-ID'  # Replace with your actual instance ID
    log_type = 'cloudwatch-logs'
    
    # Get the current timestamp for uniqueness
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Generate the S3 key (file path) dynamically
    s3_key = f"logs/{instance_id}/{log_type}-{timestamp}.json"
    
    # Extract CloudWatch logs data from the event
    cw_data = event['awslogs']['data']
    
    # Decode the base64-encoded data
    decoded_data = base64.b64decode(cw_data)
    
    # Decompress the gzipped log data
    unzipped_data = gzip.decompress(decoded_data)
    
    # Parse the log data as JSON
    log_event = json.loads(unzipped_data)
    
    # Log event to S3
    s3.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(log_event)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Log data successfully sent to S3: {s3_key}")
    }
