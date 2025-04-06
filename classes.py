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



class FogoMotor(pg.sprite.Sprite):
    def __init__(self, surface):
        pg.sprite.Sprite.__init__(self)

        self.surface = surface
        self.indice = 0
        self.imagem = IMAGEM_FOGO
        self.image = self.imagem[self.indice]
        self.rect = self.image.get_rect()
        self.rect.x = self.surface.left + int(self.surface[2]/2) - int(self.image.get_width()/2)
        self.rect.y = self.surface.bottom
    
    def update(self):
        if self.indice > 2.9:
            self.indice = 0
        self.image = self.imagem[int(self.indice)]
        self.rect.x = self.surface.left + int(self.surface[2]/2) - int(self.image.get_width()/2)
        self.rect.y = self.surface.bottom
        self.indice += 0.25



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



class CriarRecarga():
    def __init__(self, num, grupo):
        self.num = num
        self.grupo = grupo
        self.tempo = randint(0, 40)
        self.cont = 0

    def criar_recarga(self):
        for i in range(0, self.num):
            recarga = Recarga(self.grupo)
            self.grupo.add(recarga)
    
    def uptade(self):
        self.cont += 0.1
        if self.cont > self.tempo:
            if len(self.grupo) == 0:
                self.criar_recarga()
                self.cont = 0
                self.tempo = randint(0, 40)



class Personagem(pg.sprite.Sprite):
    def __init__(self, imagem, grupo, inimigos, vida, exibir, demais, recarga, outros):
        pg.sprite.Sprite.__init__(self)

        self.imagem = imagem
        self.image = self.imagem[0]
        self.rect = self.image.get_rect()
        self.rect.x = int((LARGURA-self.image.get_width())/2)
        self.rect.y = ALTURA-(100 +self.image.get_height())

        self.grupo = grupo
        self.grupo_inimigos = inimigos
        self.grupo_vida = vida
        self.grupo_exibir = exibir
        self.grupo_demais = demais
        self.grupo_recarga = recarga
        self.grupo_outros = outros
        
        self.velocidade = 10
        self.disparos = 100
        self.distancia = 0
        self.sim = True

        self.controlar_vidas()
        self.mostrar_balas()
        self.mostrar_disparos()
        self.mostrar_distancia()

        self.fogo = FogoMotor(self.rect)
        self.grupo_demais.add(self.fogo)
    
    def lancar_arma(self, tecla):
        if tecla == pg.K_a and self.disparos > 0:
            leiser = Bala(self.rect.center, self.grupo, self.grupo_inimigos)
            self.grupo.add(leiser)
            self.som_disparo()
            self.disparos -= 1

    def som_disparo(self):
        SOM_DISPARO.play().set_volume(0.5)

    def controlar_vidas(self):
        y = 30
        self.vida1 = Vidas((33, y))
        self.vida2 = Vidas((76, y))
        self.vida3 = Vidas((119, y))

        self.grupo_vida.add(self.vida1, self.vida2, self.vida3)      
    
    def mostrar_balas(self):
        if self.sim:
            balas = Recarga(self.grupo_outros, [33, 100], 0)
            self.grupo_outros.add(balas)

    def mostrar_disparos(self):
        exibir = Exibir(self.grupo_exibir, [75,100], str(self.disparos))
    
    def mostrar_distancia(self):
        exibir = Exibir(self.grupo_exibir, [750, 50], str(self.distancia))
    
    def update(self, tecla):

        self.image = self.imagem[0]

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
            self.image = self.imagem[1]

        if pg.sprite.spritecollide(self, self.grupo_recarga, 1):
            self.disparos += 1
            self.mostrar_disparos()
        
        self.distancia += int(self.velocidade/10)
        self.grupo_exibir.empty()
        self.mostrar_disparos()
        self.mostrar_distancia()



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
            SOM_IMPACTO.play().set_volume(0.3)



class Meteoro(pg.sprite.Sprite):
    def __init__(self, grupo, velocidade=5):
        pg.sprite.Sprite.__init__(self)

        self.image = IMAGEM_METEORO[randint(0,9)]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, (LARGURA-self.image.get_width()))
        self.rect.bottom = randint(-500, 0)

        self.grupo = grupo

        self.velocidade = velocidade
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.grupo.remove(self)
         


class CriarInimigos():
    def __init__(self, num, grupo):
        self.num = num
        self.grupo = grupo

    def criar_inimigo(self, aceleracao=0):
        velo = 5
        for i in range(0, self.num):
            if aceleracao:
                velo = randint(5, 25)
            meteoro = Meteoro(self.grupo, velo)
            self.grupo.add(meteoro)
    
    def uptade(self):
        if len(self.grupo) == 0 and self.num <= 2:
            self.num += 1
            self.criar_inimigo()
        elif len(self.grupo) == 0 and self.num > 2:
            self.num += 1
            self.criar_inimigo(1)



class Estrela(pg.sprite.Sprite):
    def __init__(self, grupo):
        pg.sprite.Sprite.__init__(self)
        self.image = IMAGEM_ESTRELA[randint(0,2)]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, (LARGURA-self.image.get_width()))
        self.rect.bottom = randint(-900, 0)

        self.grupo = grupo

        self.velocidade = 2
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.grupo.remove(self)



class CriarEstrela():
    def __init__(self, grupo):
        self.num = randint(5, 8)
        self.grupo = grupo

    def criar_estrela(self):
        for i in range(0, self.num):
            estrela = Estrela(self.grupo)
            self.grupo.add(estrela)
    
    def update(self):
        if len(self.grupo) == 0:
            self.criar_estrela()


class JogoPerdeu():
    def __init__(self):
        self.janela_principal = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)

        self.grupo_personagem = pg.sprite.GroupSingle()
        self.grupo_estrela = pg.sprite.Group()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_inimigos = pg.sprite.Group()
        self.grupo_vidas = pg.sprite.Group()
        self.grupo_recarga = pg.sprite.Group()
        self.grupo_exibir = pg.sprite.Group()
        self.grupo_demais = pg.sprite.Group()
        self.grupo_outros = pg.sprite.Group()
        
        self.nave = Personagem(
            IMAGEM_PERSONAGEM,
            self.grupo_disparos,
            self.grupo_inimigos,
            self.grupo_vidas,
            self.grupo_exibir,
            self.grupo_demais,
            self.grupo_recarga,
            self.grupo_outros,
        )
        self.grupo_personagem.add(self.nave)

        self.estrela = CriarEstrela(self.grupo_estrela)
        self.estrela.criar_estrela()

        MUSICA.play()

        self.rodar()

    def rodar(self):
        relogio = pg.time.Clock()
        continuar = True
        while continuar:
            relogio.tick(24)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    continuar = False
                    pg.quit()
                    exit()
            
            pg.display.flip()
            self.janela_principal.blit(FUNDO, (0,0))

            self.grupo_estrela.draw(self.janela_principal)
            self.grupo_personagem.draw(self.janela_principal)
           
            self.grupo_demais.draw(self.janela_principal)
            
            self.grupo_demais.update()
            self.grupo_estrela.update()
            self.estrela.update()
           


class Jogo():
    def __init__(self):
        self.janela_principal = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITULO)

        self.grupo_personagem = pg.sprite.GroupSingle()
        self.grupo_estrela = pg.sprite.Group()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_inimigos = pg.sprite.Group()
        self.grupo_vidas = pg.sprite.Group()
        self.grupo_recarga = pg.sprite.Group()
        self.grupo_exibir = pg.sprite.Group()
        self.grupo_demais = pg.sprite.Group()
        self.grupo_outros = pg.sprite.Group()
        
        self.nave = Personagem(
            IMAGEM_PERSONAGEM,
            self.grupo_disparos,
            self.grupo_inimigos,
            self.grupo_vidas,
            self.grupo_exibir,
            self.grupo_demais,
            self.grupo_recarga,
            self.grupo_outros,
        )
        self.grupo_personagem.add(self.nave)

        self.inimigos = CriarInimigos(1, self.grupo_inimigos)
        self.inimigos.criar_inimigo()

        self.recarga = CriarRecarga(1, self.grupo_recarga)
        self.recarga.criar_recarga()

        self.estrela = CriarEstrela(self.grupo_estrela)
        self.estrela.criar_estrela()

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

            self.grupo_estrela.draw(self.janela_principal)
            self.grupo_disparos.draw(self.janela_principal)
            self.grupo_personagem.draw(self.janela_principal)
            self.grupo_inimigos.draw(self.janela_principal)
            self.grupo_vidas.draw(self.janela_principal)
            self.grupo_recarga.draw(self.janela_principal)
            self.grupo_exibir.draw(self.janela_principal)
            self.grupo_demais.draw(self.janela_principal)
            self.grupo_outros.draw(self.janela_principal)
            
            self.grupo_personagem.update(tecla)
            self.grupo_disparos.update()
            self.grupo_inimigos.update()
            self.grupo_recarga.update()
            self.grupo_demais.update()
            self.grupo_vidas.update()
            self.grupo_exibir.update()
            self.grupo_estrela.update()
            self.grupo_outros.update()
            self.inimigos.uptade()
            self.recarga.uptade()
            self.estrela.update()

            if len(self.nave.grupo_vida.sprites()) == 0:
                continuar = False
                JogoPerdeu()



Jogo()
