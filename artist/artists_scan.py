import boto3

def scan_musics( dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('musics')
    response = table.scan(
    )
    return response['Items']

if __name__ == '__main__':
    musics = scan_musics()
    for music in musics:
        print(f'Artista {music["artist"]}:')
        for title in music["music_list"]:
            print(f'  Música: {title["title"]}')

