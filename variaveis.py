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

imagem_personagem = pg.image.load('imagens/playerShip1_blue.png')
imagem_personagem1 = pg.image.load('imagens/playerShip1_damage1.png')
IMAGEM_PERSONAGEM =[imagem_personagem, imagem_personagem1]

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

imagem_meteoro1 = pg.image.load('imagens/meteorBrown_big1.png')
imagem_meteoro2 = pg.image.load('imagens/meteorBrown_big2.png')
imagem_meteoro3 = pg.image.load('imagens/meteorBrown_big3.png')
imagem_meteoro4 = pg.image.load('imagens/meteorBrown_big4.png')
imagem_meteoro5 = pg.image.load('imagens/meteorBrown_med1.png')
imagem_meteoro6 = pg.image.load('imagens/meteorBrown_med3.png')
imagem_meteoro7 = pg.image.load('imagens/meteorBrown_small1.png')
imagem_meteoro8 = pg.image.load('imagens/meteorBrown_small2.png')
imagem_meteoro9 = pg.image.load('imagens/meteorBrown_tiny1.png')
imagem_meteoro10 = pg.image.load('imagens/meteorBrown_tiny2.png')

IMAGEM_METEORO = [
    imagem_meteoro1, imagem_meteoro2, imagem_meteoro3,
    imagem_meteoro4, imagem_meteoro5, imagem_meteoro6,
    imagem_meteoro7, imagem_meteoro8, imagem_meteoro9,
    imagem_meteoro10,
]

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
