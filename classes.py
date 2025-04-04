# O arquivo com as classes para jogo.

from sys import exit
from random import randint
import pygame as pg

from variaveis import *


pg.init()



class Numero(pg.sprite.Sprite):
    def __init__(self, grupo, pos, num):
        pg.sprite.Sprite.__init__(self)

        self.image = IMAGEM_NUM[num]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.bottom = pos[1]

        self.grupo = grupo
        self.grupo.add(self)



class Exibir():
    def __init__(self, grupo, pos, num):
        self.grupo = grupo
        self.pos = pos
        self.num = num

        self.criar_exibicao()
    
    def criar_exibicao(self):
        x = self.pos[0]
        y = self.pos[1]
        for i in range(len(self.num)):
            numero = Numero(self.grupo, [x, y], num=(int(self.num[i])))
            self.grupo.add(numero)
            x += 19 + 10



class Vidas(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = IMAGEM_VIDA
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Recarga(pg.sprite.Sprite):
    def __init__(self, grupo, pos=[0,0], velocidade=5):
        pg.sprite.Sprite.__init__(self)
        self.image = IMAGEM_RECARGA
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        if pos != [0,0]:
            self.rect.x = pos[0]
            self.rect.bottom = pos[1]
        else:
            self.rect.x = randint(0, (LARGURA-self.image.get_width()))
            self.rect.bottom = randint(-100, 0)

        self.grupo = grupo 

        self.velocidade = velocidade
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.grupo.remove(self)



class Personagem(pg.sprite.Sprite):
    def __init__(self, imagem, grupo, inimigos, vida, recarga, demais):
        pg.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = int((LARGURA-self.image.get_width())/2)
        self.rect.y = ALTURA-(100 +self.image.get_height())

        self.grupo = grupo
        self.grupo_inimigos = inimigos
        self.grupo_vida = vida
        self.grupo_recarga = recarga
        self.grupo_demais = demais
        
        self.velocidade = 10
        self.disparos = 10

        self.controlar_vidas()
        self.mostrar_balas()
        self.mostrar_disparos()
    
    def lancar_arma(self, tecla):
        if tecla == pg.K_a:
            leiser = Bala(self.rect.center, self.grupo, self.grupo_inimigos)
            self.grupo.add(leiser)
            self.som_disparo()

    def som_disparo(self):
        SOM_DISPARO.play().set_volume(0.5)

    def controlar_vidas(self):
        y = 30
        self.vida1 = Vidas((33, y))
        self.vida2 = Vidas((76, y))
        self.vida3 = Vidas((119, y))

        self.grupo_vida.add(self.vida1, self.vida2, self.vida3)      
    
    def mostrar_balas(self):
        balas = Recarga(self.grupo_demais, [33, 100], 0)
        self.grupo_demais.add(balas)

    def mostrar_disparos(self):
        exibir = Exibir(self.grupo_recarga, [75,100], str(self.disparos))
    
    def update(self, tecla):

        if tecla == pg.K_LEFT:
            self.rect.x -= self.velocidade
        elif tecla == pg.K_RIGHT:
            self.rect.x += self.velocidade
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA
        
        if pg.sprite.spritecollide(self, self.grupo_inimigos, 1):
            n = list()
            for i in self.grupo_vida.sprites():
                n.append(i)
            self.grupo_vida.remove(n[-1])
        if pg.sprite.spritecollide(self, self.grupo_demais, 1):
            print(self.grupo_recarga.sprites())
            self.disparos += 1
            self.grupo_recarga.empty()
            self.mostrar_disparos()
            print(self.grupo_recarga.sprites())




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

        self.tem_variavel = 0
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.bottom < 0:
            self.grupo.remove(self)
        if self.tem_variavel:
                self.grupo.remove(self)
        if pg.sprite.spritecollide(self, self.grupo_inimigos, 1):
            x, y = (self.rect.left, self.rect.top)
            self.image = IMAGEM_BALA_ACERTO[randint(0,2)]
            self.rect.topleft = (x-(self.image.get_width()/2)), (y-(self.image.get_height()/2))
            self.tem_variavel = 1



class Meteoro(pg.sprite.Sprite):
    def __init__(self, grupo):
        pg.sprite.Sprite.__init__(self)

        self.image = IMAGEM_METEORO
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, (LARGURA-self.image.get_width()))
        self.rect.bottom = randint(-100, 0)

        self.grupo = grupo

        self.velocidade = 5
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.grupo.remove(self)
           


class CriarInimigos():
    def __init__(self, num, grupo):
        self.num = num
        self.grupo = grupo

    def criar_inimigo(self):
        for i in range(0, self.num):
            meteoro = Meteoro(self.grupo)
            self.grupo.add(meteoro)
    
    def uptade(self):
        if len(self.grupo) == 0:
            self.num += 1
            self.criar_inimigo()



class Jogo():
    def __init__(self):
        self.janela_principal = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)

        self.grupo_personagem = pg.sprite.GroupSingle()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_inimigos = pg.sprite.Group()
        self.grupo_vidas = pg.sprite.Group()
        self.grupo_recarga = pg.sprite.Group()
        self.grupo_demais = pg.sprite.Group()
        
        self.nave = Personagem(
            IMAGEM_PERSONAGEM,
            self.grupo_disparos,
            self.grupo_inimigos,
            self.grupo_vidas,
            self.grupo_recarga,
            self.grupo_demais,
        )
        self.grupo_personagem.add(self.nave)

        self.inimigos = CriarInimigos(1, self.grupo_inimigos)
        self.inimigos.criar_inimigo()

        recarga = Recarga(self.grupo_demais)
        self.grupo_demais.add(recarga)

        MUSICA.play()

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
            self.grupo_vidas.draw(self.janela_principal)
            self.grupo_recarga.draw(self.janela_principal)
            self.grupo_demais.draw(self.janela_principal)
            
            self.grupo_personagem.update(tecla)
            self.grupo_disparos.update()
            self.grupo_inimigos.update()
            self.grupo_recarga.update()
            self.grupo_demais.update()
            self.grupo_vidas.update()
            self.inimigos.uptade()


Jogo()
