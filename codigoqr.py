import qrcode

PG_BLUE = (27, 54, 87)
PG_GREEN = (0, 174, 150)

dados = {
    'github': 'seugithub',
    'linkedin': 'seulinkedin',
    'gmail': 'seuemail'
}

if __name__ == '__main__':
    cores = [(PG_BLUE, 'white'), ('white', PG_GREEN), (PG_GREEN, PG_BLUE)]
    for i, (chave, valor) in enumerate(dados.items()):
        qr = qrcode.QRCode(None, qrcode.ERROR_CORRECT_H)
        qr.add_data(valor)
        img = qr.make_image(fill_color=cores[i][0], back_color=cores[i][1])
        img.save(f'{chave}.png')