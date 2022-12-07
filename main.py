from pantallas import Partida,Menu
import pygame as pg





menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == "jugar":
    juego = Partida()
    juego.bucle_forograma()