def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

import boto3
import json
session = boto3.Session(profile_name='default',region_name='us-west-2')
client = session.client('dynamodb')

# read file
with open('seed_data_dynamodb.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

for x in batch(obj['Test'], 25):
    subbatch_dict = {'Test': x}
    response = client.batch_write_item(RequestItems=subbatch_dict)
