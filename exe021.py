'''faca um programa em pythn que abra e reproduza uma musica tocando um MP3'''
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('exe06.mp3')
pygame.mixer.music.play()
pygame.event.wait()

