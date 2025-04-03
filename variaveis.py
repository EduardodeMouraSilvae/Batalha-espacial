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

IMAGEM_BALA = pg.image.load('imagens/laserBlue01.png')
IMAGEM_BALA_ACERTO = pg.image.load('imagens/laserBlue08.png')

IMAGEM_METEORO = pg.image.load('imagens/meteorBrown_big1.png')

# Sons
SOM_DISPARO = pg.mixer.Sound('sons/sfx_laser1.ogg')


# Músicas
MUSICA = pg.mixer.Sound('sons/OutThere.ogg')