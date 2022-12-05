import pygame as pg
from figura_class import Pelota, Raqueta

ANCHO = 800
ALTO = 600

class Partida():
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("PONG")      
        self.tasa_refresco = pg.time.Clock()
        
        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=0.5,vy=0.5)

        self.raqueta1 = Raqueta(10,300,color=(191,20,12),vx=2,vy=2)
        self.raqueta2 = Raqueta(790,300,color=(22,238,234),vx=2,vy=2)
        
    def bucle_forograma(self):
        game_over = False
        
        while not game_over:
            self.tasa_refresco.tick(800)
            
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = True
                    
            self.raqueta1.mover(pg.K_w,pg.K_s)      
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.pelota.mover()
            
            self.pantalla_principal.fill((8, 130, 28))

            self.pelota.comprobar_choque(self.raqueta1,self.raqueta2)

            self.pelota.marcador(self.pantalla_principal)
            
            cont_linea1 = 0
            cont_linea2 = 53
            while cont_linea1 <= 560 and cont_linea2 <= 630:
                pg.draw.line(self.pantalla_principal,(255,255,255),(400,cont_linea1),(400,cont_linea2),width=10)
                cont_linea1 += 70
                cont_linea2 += 70

            self.pelota.dibujar(self.pantalla_principal)


            self.raqueta1.dibujar(self.pantalla_principal)


            self.raqueta2.dibujar(self.pantalla_principal)
        
            pg.display.flip()
        pg.quit        
    