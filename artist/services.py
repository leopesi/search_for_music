from lyricsgenius import Genius
import os

""" 
Para iniciar o DynamoDB em seu computador, abra uma janela de prompt de comando,
vá até o diretório onde você extraiu o DynamoDBLocal.jar e insira o seguinte comando:
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
"""
class Get_Genius():
    def get_popularity_songs(artist_name: str, max_songs: int, sort="popularity"):
        genius = Genius(os.environ.get('API_PASSWORD'))
        artist = genius.search_artist(artist_name, max_songs=max_songs, sort=sort, get_full_info=True,)
        return artist.songs