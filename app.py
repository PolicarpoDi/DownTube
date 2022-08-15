## Para importar o modulo PYTUBE
from pytube import YouTube
from pytube.cli import on_progress
import os


resp = input('Deseja fazer o donwload de algum vídeo? ')
while (resp == 's'):
    # Para inserir o url de um vídeo do Toutube
    link = input("Insira o link desejado: ")

    path_padrao = '~/Vídeos/Downtube'
    # Selecione o diretório para salvar o vídeo
    path = input(f'Informe o diretório para salvar o vídeo: {path_padrao}')

    # Para mostrar o progresso do Download
    yt = YouTube(link, on_progress_callback=on_progress)

    # Para mostrar o título do vídeo
    print('Título = ', yt.title)

    # Para mostrar que ja iniciou o download
    print('Baixando...')

    # Para baixar a maior resolução do vídeo que pretende baixar
    ys = yt.streams.get_highest_resolution()
    ys.download(path)
    print(f'Download {yt.title} finalizado -> ')
    print('----------------------------')
    print()
    resp = input('Deseja continuar? ')
else:
    print('Finalizado')


# Caso apresente o erro "'NoneType' object has no attribute 'download'" é devido problema no link
# Inserir barra de progresso a Barra de progresso