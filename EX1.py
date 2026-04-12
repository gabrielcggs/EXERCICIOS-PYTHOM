import pygame

pygame.mixer.init()

arquivo = "musica.mp3"
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
