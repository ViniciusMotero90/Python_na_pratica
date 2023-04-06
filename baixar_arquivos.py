import requests
import os

def baixa_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em {}".format(endereco))

if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf'
    OUTPUT_DIR = 'downloads'
    for i in range(1, 26):
        nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        baixa_arquivo(BASE_URL.format(i), nome_arquivo)
