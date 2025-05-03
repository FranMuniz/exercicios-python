'''Escreva um programa em Python que abra e reproduza o áudio de um arquivo mp3'''

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('hey_brother.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Pressione Enter para encerrar...')