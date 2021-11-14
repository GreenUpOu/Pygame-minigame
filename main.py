import pygame
from teleport import teleport


class character:

    def __init__(self, x, y):
        self.w = ye
        self.h = 1.5*ye
        self.x = x
        self.y = y
        self.dy = 0

    def jump(self):
        self.dy = -ye//2.8

    def falling(self):
        global jumping
        if self.x >= ye//4 and self.x < 2*ye and self.y + self.h + self.dy >= 8.25*ye:
            self.y = 8.25*ye - self.h
            self.dy = 0
            jumping = False
        elif self.x + self.w > floor[8.25*ye][2] and self.y + self.h + self.dy >= 8.25*ye:
            self.y = 8.25*ye - self.h
            self.dy = 0
            jumping = False
        elif self.y + self.h + self.dy < 4*ye:
            self.y += self.dy
            self.dy += g
        elif self.y >= 5*ye:
            if self.y + self.h + self.dy <= 8.5*ye:
                self.y += self.dy
                self.dy += g
            else:
                self.y = 8.5*ye - self.h
                self.dy = 0
                jumping = False
        elif self.y + self.w//2 <= 4*ye and self.x + self.w > floor[4*ye][0] and self.x < floor[4*ye][1]:
            jumping = False
            self.y = 4*ye - self.h
            self.dy = 0
        else:
            self.y += self.dy
            self.dy += g

    def Move_left(self):
        if self.x - ye//12 <= ye//4:
            self.x = ye//4
        else:
            self.x -= ye//12

    def Move_right(self):
        if self.x + self.w + ye//12 >= 15.75*ye:
            self.x = 15.75*ye - self.w
        else:
            self.x += ye//12





pygame.init()
clock = pygame.time.Clock()
FPS = 60
blue = (0, 0, 255)
yellow = (0, 255, 0)

sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
print(sc.get_width(), sc.get_height())


bg = pygame.image.load("final.png")


ye = sc.get_width() / 16
floor = {8.5*ye: True, 4*ye: [3*ye, 13*ye], 8.25*ye:[ye/4, 2*ye,14*ye, 15.75*ye]}
left_wall = {ye//4 : True, 13*ye: [4*ye, 5*ye], 2*ye: [8.25*ye, 8.5*ye]}
right_wall = {15.75*ye: True, 3*ye: [4*ye, 5*ye], 14*ye: [8.25*ye, 8.5*ye]}
g = ye//24
jumping = True
player = character(7*ye, 6*ye)
teleport1 = teleport(ye//4, 8.25*ye, 3.5*ye, 2.5*ye, 1.75*ye, 0.25*ye)
teleport2 = teleport(14*ye, 8.25*ye, 11.5*ye, 2.5*ye, 1.75*ye, 0.25*ye)

pygame.display.update()
pygame.display.set_caption("FIGHTING")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    if keys[pygame.K_w] and not jumping and player.dy == 0:
        jumping = True
        player.jump()
    if keys[pygame.K_a]:
        player.Move_left()
    elif keys[pygame.K_d]:
        player.Move_right()

    sc.blit(bg, [0, 0])#потом переставить после всех процессов, это просто чтобы было видно кд портала
    teleport1.process(player)
    teleport2.process(player)

    player.falling()



    '''pygame.draw.rect(sc, blue, (0, 0, 16 * ye, ye / 2))
    pygame.draw.rect(sc, blue, (0, 8.5 * ye, 16 * ye, ye / 2))
    pygame.draw.rect(sc, blue, (0, 0, ye/4, 9*ye))
    pygame.draw.rect(sc, blue, (15.75*ye, 0, ye/4, 9*ye))
    pygame.draw.rect(sc,blue, (3*ye, 4*ye,10*ye, ye))
    pygame.draw.rect(sc,yellow, (ye/4, 8.25*ye, 1.75*ye, ye*0.5))
    pygame.draw.rect(sc, yellow, (14*ye, 8.25 * ye, 1.75*ye, ye*0.5))
    pygame.draw.rect(sc, yellow, (3*ye, 0, 1.75*ye, ye / 2))
    pygame.draw.rect(sc, yellow, (11.25 * ye, 0 , 1.75*ye, ye / 2))'''

    pygame.draw.rect(sc, (1,123,17), (player.x, player.y, player.w, player.h))

    pygame.display.update()
    clock.tick(FPS)

pygame.display.update()
pygame.quit()
quit()
