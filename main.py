import pygame
import sys
import controls
from character import Character


def run():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))   #sizes
    pygame.display.set_caption('gg')  #tite
    bg_color = (0,100,200)
    character = Character(screen)

    while True:
        controls.events(character)
        character.update_character()
        screen.fill(bg_color)
        character.output()
        pygame.display.flip()





run()