import pygame
import sys


def events(character):


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character.mleft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                character.mleft = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                character.mright = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                character.mright = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                character.mup = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                character.mup = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                character.mdown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                character.mdown = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                character.mleft2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                character.mleft2 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                character.mright2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_k:
                character.mright2 = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                character.mup2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_u:
                character.mup2 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                character.mdown2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_j:
                character.mdown2 = False