# Arquivo com as variáveis do jogo
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