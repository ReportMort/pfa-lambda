from __future__ import print_function
import json
import uuid
import boto3
from titus.genpy import PFAEngine

print('Creating Scoring Engine')

# download the model
bucket = 'my-pfa-models'
key = 'model.pfa'
download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
s3_client = boto3.client('s3')
s3_client.download_file(bucket, key, download_path)

# create a scoring engine
engine, = PFAEngine.fromJson(json.load(open(download_path)))

print('Finished Creating Scoring Engine')

def lambda_handler(event, context):

    # score the event JSON data provided to this function
    return engine.action(event)
