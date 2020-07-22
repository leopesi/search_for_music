from artist.services import Get_Genius
import uuid
import boto3
from django.http import JsonResponse, HttpResponse

def artist(request, name, dynamodb=None):
    if request.method == "GET":
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        genius = Get_Genius
        dados = genius.get_popularity_songs(name, max_songs=2)
        id = str(uuid.uuid4())
        content2 = [
            {
                "title": dado.title,

            }
            for dado in dados
        ]
        item = {"id": id,
                "artist": name,
                "music_list": content2
                }

        table = dynamodb.Table('musics')
        table.put_item(Item=item)

        return JsonResponse(item, safe=False)

    else:
        return HttpResponse('Erro de operação - Requeste != GET')