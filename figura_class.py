import pygame as pg

class Pelota():
    def __init__(self,pos_x,pos_y,radio=10,color=(231,23,238),vx=0.5,vy=0.5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
       
        self.font = pg.font.Font(None, 40)
        
    def mover(self,y_max = 600, x_max = 800):
        
        self.pos_x += self.vx
                              # velocidad la pelota, para que se mueva
        self.pos_y += self.vy
                                                                                
        if self.pos_y >= y_max - self.radio  or self.pos_y <= 0 + self.radio: # Para que la pelota rebote en los limites de y
            self.vy *= -1                                                     # de arriba a abajo
        
        if self.pos_x >= x_max + self.radio * 10: # limite derecha                
            
            self.pos_x = x_max // 2
                                    #Para que la pelota salga del centro de la pantalla
            self.pos_y = y_max // 2    
            
            self.vx *= -1 # para cambiar la direccion de la pelota                                       
            self.vy *= -1 # ponemos vy para que la pelota salga hacia    
                          # el mismo lado de donde llego                 # Para que la pelota desaparezca mas alla de los limites de x
            return "right"                                               # y vuelva a aparecer rebotando hacia el lado contrario
        if self.pos_x < 0 - self.radio * 10: #Limite izquierdo           # desde donde vino                                   
          
            self.pos_x = x_max // 2 #
                                    #Para que la pelota salga del centro de la pantalla
            self.pos_y = y_max // 2 #   
    
            self.vx *= -1 # para cambiar la direccion de la pelota                   
            self.vy *= -1 # ponemos vy para que la pelota salga hacia                                                                                    
                          # el mismo lado de donde llego        
            return "left"
                                                   
    def dibujar(self, pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)#Dibujar la pelota
        
    @property #Decorador hace que podamos invocar una función como una varable osea sin los parentecis, solo el rsultado
    def derecha(self):
        return self.pos_x + self.radio
    @property 
    def izquierda(self):
        return self.pos_x - self.radio
    @property                                   #Cordenadas de los mismos objetos como tal para 
    def arriba(self):                           #implementar el choque pelota con raqueta
        return self.pos_y - self.radio
    @property   
    def abajo(self):
        return self.pos_y + self.radio
     
    def comprobar_choque(self,r1,r2):#Para tener varios parametros ponemos el * antes, signifaca que tendriamos r1 y r2
        #Logica de chaque pelota raqueta derecha
        
        if self.derecha >= r2.izquierda and \
            self.izquierda <= r2.derecha and \
            self.abajo >= r2.arriba and \
            self.arriba <= r2.abajo:
                self.vx *= -1
               
        if self.derecha  >= r1.izquierda and \
            self.izquierda  <= r1.derecha and \
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
            self.vx *= -1
            
    def comprobar_choqueV2(self,*raquetas):#Para tener varios parametros ponemos el * antes, signifaca que tendriamos r1 y r2
                                           #Logica de chaque pelota raqueta derecha
         for r in raquetas:
             if self.derecha  >= r.izquierda and \
                self.izquierda  <= r.derecha and \
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                     self.vx *= -1
                     break    
            
            
class Raqueta():
    def __init__(self,pos_x, pos_y, w = 20, h= 100, color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
    
    def mover(self,tecla_arriba,tecla_abajo,y_max = 600, y_min = 0):
        estado_teclas = pg.key.get_pressed()
        
        # Mover las teclas de arriba abajo --- para poner limite a la raqueta y no se salga de la pantalla en y
        if estado_teclas[tecla_arriba] == True and self.pos_y > y_min + self.h//2: 
            self.pos_y -= self.vy                                        
        elif estado_teclas[tecla_abajo] == True and self.pos_y < y_max - self.h//2:
            self.pos_y += self.vy
        
    def dibujar(self,pantalla):
          pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))#Dibujar la raqueta
          
     
    @property #Decorador hace que podamos invocar una función como una varable osea sin los parentecis,solo te pone el resultado directamente    
    def arriba(self):
        return self.pos_y - self.h//2  
    @property   
    def abajo(self):                               #Cordenadas de los mismos objetos como tal para 
        return self.pos_y + self.h//2              #implementar el choque raqueta  con pelota
    @property 
    def izquierda(self):
        return self.pos_x - self.w//2
    @property
    def derecha(self):
        return self.pos_x + self.w//2
   
   
    