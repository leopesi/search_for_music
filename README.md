# Search_for_music

 API em Python (DJANGO) que consume a API do Genius e que dado um nome lista as 10 músicas mais populares do artista pesquisado, salvando um id de transação no formato uuid versão 4, nome do artista pesquisado, em uma coleção no DynamoDB.
 
 ## Recursos utilizados - *Built with*
- [x] Python 3.8
- [x] Django 3.0
- [x] AWS - Dynamodb  

## Como instalar? - *How to install?*

**Clone o repositório.**
*Clone this repository*

$ git clone https://github.com/leopesi/search_for_music.git

**Crie um virtualenv** - *Creating a virtialenv*

- 'pip install virtualenv'
- virtualenv nome_da_virtualenv

**Ativando uma virtualenv** - *Activating a virtialenv*

- souce nome_da_virtualenv/bin/activate (Linux ou macOS)
- nome_da_virtualenvScriptsactivate (Windows)

**Instale as depêndencias.** - *Installing dependencies*
- pip install -r requirements.txt
