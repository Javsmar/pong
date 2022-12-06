import pygame as pg
from figura_class import Pelota, Raqueta

ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
NARANJA = (202,111,30)
VERDE = (8,130,28)

class Partida():
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("PONG")      
        self.tasa_refresco = pg.time.Clock()
        
        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=1.5,vy=1.5)

        self.raqueta1 = Raqueta(10,300,color=(191,20,12),vx=2,vy=2)
        self.raqueta2 = Raqueta(790,300,color=(22,238,234),vx=2,vy=2)
        
        self.font = pg.font.Font(None, 30)
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        
    def bucle_forograma(self):
        game_over = False
        
        while not game_over:
            self.tasa_refresco.tick(280)
            
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = True
                    
            self.raqueta1.mover(pg.K_w,pg.K_s)      
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            
            self.quienMarco = self.pelota.mover()
             
            self.pantalla_principal.fill((VERDE))
            
            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)
            self.marcador()
            self.line_disc()
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
        

            pg.display.flip()
            
        pg.quit() 
        
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
        self.pantalla_principal.blit(player1,(125,10)) 
        self.pantalla_principal.blit(player2,(530,10)) 
    
    def marcador(self):  
        if self.quienMarco == "right":
            self.marcador2 += 1
        elif self.quienMarco == "left":
            self.marcador1 += 1
        marcadorIzquierdo = self.font.render(str(self.marcador1), 0, (NARANJA))
        marcadorDerecha = self.font.render(str(self.marcador2), 0, (NARANJA))
        self.pantalla_principal.blit(marcadorDerecha,(170,40))  
        self.pantalla_principal.blit(marcadorIzquierdo,(575,40))