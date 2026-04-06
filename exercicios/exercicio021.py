import pygame

pygame.init()
pygame.mixer.music.load('exercicio021.mp3')
pygame.mixer.music.play()

# Keep the program running while the music plays
input("Press Enter to exit...")