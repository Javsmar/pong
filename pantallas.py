import pygame as pg
from figura_class import Pelota, Raqueta
from utils import *

class Partida:
    
    def __init__(self):
       
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("PONG")      
        self.tasa_refresco = pg.time.Clock()
        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=1.5,vy=1.5)
        self.raqueta1 = Raqueta(10,300,color=(ROJO),vx=2,vy=2)
        self.raqueta2 = Raqueta(790,300,color=(AZUL),vx=2,vy=2)
        self.font = pg.font.Font("fonts/pressStart2P.ttf",25)
        self.fuenteTemp = pg.font.Font("fonts/pressStart2P.ttf",30)
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        self.temporizador = TIEMPO_LIMITE # en  milisegundos
        self.colorFondo = VERDE
        self.contadorFotograma = 0
        
    def bucle_fotograma(self):
        game_over = False
        
        while not game_over and (self.marcador1 < 5 or self.marcador2 < 5 ) and self.temporizador > 0:
            
            
            salto_tiempo = self.tasa_refresco.tick(FPS)
            
            self.temporizador -= salto_tiempo
            
            if self.temporizador == 0:
                game_over = True
            
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = True
                    
            self.raqueta1.mover(pg.K_w,pg.K_s)      
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.quienMarco = self.pelota.mover()
            
            
             
            self.pantalla_principal.fill(self.fijar_fondo())
            
            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)
            
            self.marcador()
            self.line_disc()
            
            time = self.font.render("TIME  ", 0, (AMARILLO)) 
            self.pantalla_principal.blit(time,(350,10))
            tiempo = self.font.render(str(int(self.temporizador/1000)), 0, (ROJO)) 
            self.pantalla_principal.blit(tiempo ,(390,40)) 
            
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
            
           

            pg.display.flip()
            
        return self.resultado_final()
    
       
        
    def line_disc(self):
        cont_linea1 = 0
        cont_linea2 = 50
        while cont_linea1 <= 560 and cont_linea2 <= 630:
            pg.draw.line(self.pantalla_principal,(BLANCO),(400,cont_linea1),(400,cont_linea2),width=10)
            cont_linea1 += 70
            cont_linea2 += 70

        
    def mostrar_jugador(self):
        player1 = self.font.render("PLAYER 1  ", 0, (NARANJA)) 
        player2 = self.font.render("PLAYER 2  ", 0, (NARANJA))
        self.pantalla_principal.blit(player1,(95,10)) 
        self.pantalla_principal.blit(player2,(505,10)) 
    
    def marcador(self):  
        if self.quienMarco == "right":
            self.marcador2 += 1
        elif self.quienMarco == "left":
            self.marcador1 += 1
            
        marcadorIzquierdo = self.font.render(str(self.marcador1), 0, (NARANJA))
        marcadorDerecha = self.font.render(str(self.marcador2), 0, (NARANJA))
        self.pantalla_principal.blit(marcadorDerecha,(170,40))  
        self.pantalla_principal.blit(marcadorIzquierdo,(580,40))
        
    def fijar_fondo(self):#Para que parpedee la pantalla a medida que el tiempo se acaba
        self.contadorFotograma += 1#creamos un contador  para que itere y pueda parpadear
        
        if self.temporizador > primer_aviso:# no entra en ninguna condición
            self.contadorFotograma = 0
            
        elif self.temporizador > segundo_aviso:#entra en la condición que parpadee en 10 seg
             if self.contadorFotograma == 70:
                if self.colorFondo == VERDE:
                    self.colorFondo = NARANJA
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0
            
        else:# entra en la condicion que parpadee en rojo, 5 SEGUNDOS
            if self.contadorFotograma == 70:
                if self.colorFondo == VERDE:
                    self.colorFondo = ROJO
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0

        return self.colorFondo
    
    def resultado_final(self):
        if self.marcador1 > self.marcador2:
            return f"Gana el Jugador 2, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"
        elif self.marcador2 > self.marcador1:
            return f"Gana el Jugador 1, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"
        else:      
            return f"Empate, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"
    
class Menu:
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Menu")
        self.tasa_refresco = pg.time.Clock()

        self.imagenFondo = pg.image.load("image/portada.jpg")
        self.fuenteMenu = pg.font.Font("fonts/pressStart2P.ttf", 20)

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                    elif evento.key == pg.K_r:
                        game_over = True
           
            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar",0,PINK)
            record = self.fuenteMenu.render("Pulsa R para ver records",0,PINK)
            self.pantalla_principal.blit(jugar, (10,ALTO//2) )
            self.pantalla_principal.blit(record, (10,ALTO//1.8) )
            pg.display.flip()
            
class Resultado:
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()

        #self.imagenFondo = pg.image.load("image/portada.jpg")
        self.fuenteResultado = pg.font.Font("fonts/pressStart2P.ttf", 15)
        self.resultado = ""

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                        return "jugar"          

            self.pantalla_principal.fill(BLANCO)
            result = self.fuenteResultado.render(self.resultado,0,PINK)
            self.pantalla_principal.blit(result, (10,ALTO//2) )
            pg.display.flip()
      
    def  recibir_resultado(self,resultado):
              self.resultado = resultado
              
class Records:
    def __init__(self):
      
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Records")
        self.tasa_refresco = pg.time.Clock()

        #self.imagenFondo = pg.image.load("image/portada.jpg")
        self.fuenteResultado = pg.font.Font("fonts/pressStart2P.ttf", 15)
      

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    game_over = True
                             

            self.pantalla_principal.fill(BLANCO)
            result = self.fuenteResultado.render("RECORDS",0,PINK)
            self.pantalla_principal.blit(result, (10,ALTO//2) )
            pg.display.flip()
            
            