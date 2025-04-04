# Arquivo com as variáveis do jogo
# nomes: TIPO_CLASSE, ex.: IMAGEM_OBJETO
import pygame as pg


pg.init()

# Dimensões
LARGURA = 32 * 30
ALTURA = 32 * 30

# Nomes
TITULO = 'Batalha Espacial'

# Imagens
fundo = pg.image.load("imagens/fundo1.png")
FUNDO = pg.transform.scale_by(fundo, 4)

IMAGEM_PERSONAGEM = pg.image.load('imagens/playerShip1_blue.png')
IMAGEM_VIDA = pg.image.load('imagens/playerLife1_blue.png')

IMAGEM_BALA = pg.image.load('imagens/laserBlue01.png')
imagem_bala_acerto1 = pg.image.load('imagens/laserBlue08.png')
imagem_bala_acerto2 = pg.image.load('imagens/laserBlue09.png')
imagem_bala_acerto3 = pg.image.load('imagens/laserBlue10.png')
IMAGEM_BALA_ACERTO = [
    imagem_bala_acerto1,
    imagem_bala_acerto2,
    imagem_bala_acerto3
]

IMAGEM_RECARGA = pg.image.load('imagens/pill_blue.png')

IMAGEM_METEORO = pg.image.load('imagens/meteorBrown_big1.png')

imagem_num_0 = pg.image.load('imagens/numeral0.png')
imagem_num_1 = pg.image.load('imagens/numeral1.png')
imagem_num_2 = pg.image.load('imagens/numeral2.png')
imagem_num_3 = pg.image.load('imagens/numeral3.png')
imagem_num_4 = pg.image.load('imagens/numeral4.png')
imagem_num_5 = pg.image.load('imagens/numeral5.png')
imagem_num_6 = pg.image.load('imagens/numeral7.png')
imagem_num_7 = pg.image.load('imagens/numeral7.png')
imagem_num_8 = pg.image.load('imagens/numeral8.png')
imagem_num_9 = pg.image.load('imagens/numeral9.png')

IMAGEM_NUM = [
    imagem_num_0, imagem_num_1, imagem_num_2,
    imagem_num_3, imagem_num_4, imagem_num_5,
    imagem_num_6, imagem_num_7, imagem_num_8, 
    imagem_num_9,
]

# Sons
SOM_DISPARO = pg.mixer.Sound('sons/sfx_laser1.ogg')


# Músicas
MUSICA = pg.mixer.Sound('sons/OutThere.ogg')