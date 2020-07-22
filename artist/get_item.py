from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_artist(artist, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('musics')

    try:
        response = table.get_item(Key={'artist': artist})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    artist = get_artist("oasis",)
    if artist:
        print("Get artist succeeded:")
        pprint(artist, sort_dicts=False)