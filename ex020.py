import pygame
# incia o pygame
pygame.init()
pygame.mixer.music.load('ex20.mp3')
pygame.mixer.music.play()
pygame.event.wait()