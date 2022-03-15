import pygame
speed1 = 3
speed2 = 6

class Character():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/12.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.mspeed1 = False
        self.mspeed2 = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_character(self):
        if self.mspeed1 == True:
            if self.mright == True:
                self.rect.centerx += speed1
            if self.mleft == True:
                self.rect.centerx -= speed1
            if self.mup == True:
                self.rect.centery -= speed1
            if self.mdown == True:
                self.rect.centery += speed1
        if self.mspeed2 == True:
            if self.mright == True:
                self.rect.centerx += speed2
            if self.mleft == True:
                self.rect.centerx -= speed2
            if self.mup == True:
                self.rect.centery -= speed2
            if self.mdown == True:
                self.rect.centery += speed2