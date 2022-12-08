from pantallas import Partida, Menu, Resultado
import pygame as pg


juego = Partida()
valor_resultado = juego.bucle_fotograma()
print("El resultado final: ",valor_resultado)
resultado = Resultado(valor_resultado)
resultado.bucle_pantalla()

"""
menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == "jugar":
    juego = Partida()
    juego.bucle_forograma()
"""