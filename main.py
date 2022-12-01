from figura_class import Pelota, Raqueta
import pygame as pg 

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")

cronometro = pg.time.Clock()#Tasa de refresco de los fotogramas por segundo de nuestro bucle

game_over = False

pelota = Pelota(400,300)

raqueta1 = Raqueta(10,300,color=(191,20,12),vx=2,vy=2)
raqueta2 = Raqueta(790,300,color=(22,238,234),vx=2,vy=2)

while not game_over:
    vt = cronometro.tick(800)#Tasa de refresco de los fotogramas por segundo de nuestro bucle
    
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
           
    pantalla_principal.fill((8, 130, 28))
    
    pg.draw.line(pantalla_principal, (255,255,255),(400,0),(400,600),width=5) 
    
    pelota.dibujar(pantalla_principal)
    pelota.mover()
    raqueta1.dibujar(pantalla_principal)
    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.dibujar(pantalla_principal)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    
    pg.display.flip()
pg.quit