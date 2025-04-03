# O arquivo com as classes para jogo.

from sys import exit
from random import randint
import pygame as pg

from variaveis import *


pg.init()



class Personagem(pg.sprite.Sprite):
    def __init__(self, imagem, grupo, inimigos):
        pg.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = int((LARGURA-self.image.get_width())/2)
        self.rect.y = ALTURA-(100 +self.image.get_height())

        self.grupo = grupo
        self.grupo_inimigos = inimigos
        
        self.velocidade = 5
    
    def lancar_arma(self, tecla):
        if tecla == pg.K_a:
            leiser = Bala(self.rect.center, self.grupo, self.grupo_inimigos)
            self.grupo.add(leiser)
            self.som_disparo()

    def som_disparo(self):
        SOM_DISPARO.play().set_volume(0.5)         
    
    def update(self, tecla):

        if tecla == pg.K_LEFT:
            self.rect.x -= self.velocidade
        elif tecla == pg.K_RIGHT:
            self.rect.x += self.velocidade
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA



class Bala(pg.sprite.Sprite):
    def __init__(self, pos, grupo, grupo_inimigos):
        pg.sprite.Sprite.__init__(self)

        self.image = IMAGEM_BALA
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]-(self.image.get_width()/2)
        self.rect.y = pos[1]-(self.image.get_height()/2)

        self.grupo = grupo
        self.grupo_inimigos = grupo_inimigos

        self.velocidade = -10
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.bottom < 0:
            self.grupo.remove(self)
        if pg.sprite.spritecollide(self, self.grupo_inimigos, 1):
            self.grupo.remove(self)



class Meteoro(pg.sprite.Sprite):
    def __init__(self, grupo):
        pg.sprite.Sprite.__init__(self)

        self.image = IMAGEM_METEORO
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, LARGURA)
        self.rect.bottom = -100

        self.grupo = grupo

        self.velocidade = 5
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            print('Sim.')
            self.grupo.remove(self)
           





class Jogo():
    def __init__(self):
        self.janela_principal = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)

        self.grupo_personagem = pg.sprite.GroupSingle()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_inimigos = pg.sprite.Group()
        self.grupo_inimigos
        
        self.nave = Personagem(IMAGEM_PERSONAGEM, self.grupo_disparos, self.grupo_inimigos)
        self.meteoro = Meteoro(self.grupo_inimigos)

        self.grupo_personagem.add(self.nave)
        self.grupo_inimigos.add(self.meteoro)

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
                    if event.key == pg.K_a:
                        self.nave.lancar_arma(tecla)
                elif event.type == pg.KEYUP:
                    tecla = 0
            
            pg.display.flip()
            self.janela_principal.blit(FUNDO, (0,0))

            self.grupo_disparos.draw(self.janela_principal)
            self.grupo_personagem.draw(self.janela_principal)
            self.grupo_inimigos.draw(self.janela_principal)
            
            self.grupo_personagem.update(tecla)
            self.grupo_disparos.update()
            self.grupo_inimigos.update()


Jogo()