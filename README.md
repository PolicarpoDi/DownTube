# **_Programa para download de vídeos no Youtube_**
#### 
>Programa simples para realizar download de qualquer vídeo do Youtube 
###
### **Como usar**
#### Crie uma venv pelo terminal:
```
virtualenv venv
```
#### Ative a venv:
```
source venv/bin/activate
```
#### Instale o pytube:
```
pip install pytube
```
#### Rode o script
~~~Python
from pytube import YouTube
from pytube.cli import on_progress

resp = input('Deseja fazer o donwload de algum vídeo? ')
while (resp == 's'):
    # Para inserir o url de um vídeo do Toutube
    link = input("Insira o link desejado: ")

    # Para mostrar o progresso do Download
    yt = YouTube(link, on_progress_callback=on_progress)

    # Para mostrar o título do vídeo
    print('Título = ', yt.title)

    # Para mostrar que ja iniciou o download
    print('Baixando...')

    # Para baixar a maior resolução do vídeo que pretende baixar
    ys = yt.streams.get_highest_resolution()
    ys.download()
    print(f'Download {yt.title} finalizado com sucesso!')
    print('----------------------------')
    print()
    resp = input('Deseja continuar? ')
else:
    print('Finalizado')
~~~

##
#### **Implementações futuras**
* _Inserir barra de progresso_ - *FEITO*
* _Selecionar diretório desejado_
###
