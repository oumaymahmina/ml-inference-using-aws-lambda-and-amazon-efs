import boto3
import os


model_dir = os.getenv('MODEL_DIR', "/mnt/ml/models/")
s3 = boto3.client('s3')

bucket_name = "ml-test-bucket-name"

def lambda_handler(event, context):
    
    if not os.path.isdir(model_dir):
        os.system('mkdir /mnt/ml/models/')

    key = event['Records'][0]['s3']['object']['key']
    
    s3.download_file(bucket_name, key, f'{model_dir}/{key}')
    
    print("ML Model file downloaded;!")

    