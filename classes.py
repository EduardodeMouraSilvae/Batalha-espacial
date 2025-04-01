# O arquivo com as classes para jogo.

from sys import exit
import pygame as pg

from variaveis import *


pg.init()



class Personagem(pg.sprite.Sprite):
    def __init__(self, imagem):
        pg.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA-(100 +self.image.get_height())
        self.rect.x = int((LARGURA-self.image.get_width())/2)

        self.velocidade = 5
    
    def update(self, tecla):
        if tecla == pg.K_LEFT:
            self.rect.x -= self.velocidade
        elif tecla == pg.K_RIGHT:
            self.rect.x += self.velocidade
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA



class Jogo():
    def __init__(self):
        self.janela_principal = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)

        nave = Personagem(IMAGEM_PERSONAGEM)

        self.grupo = pg.sprite.Group()
        self.grupo.add(nave)
        
        self.rodar()

    def rodar(self):
        relogio = pg.time.Clock()
        continuar = True
        tecla = 0
        while continuar:
            relogio.tick(24)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    continuar = False
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    tecla = event.key
                elif event.type == pg.KEYUP:
                    tecla = 0
                    
            
            pg.display.flip()
            self.janela_principal.blit(FUNDO, (0,0))
            self.grupo.draw(self.janela_principal)
            self.grupo.update(tecla)
                    