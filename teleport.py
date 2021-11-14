import pygame
class teleport:
    def __init__(self, x, y, finx, finy, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.finx = finx
        self. finy = finy
        self.passanger = False
        self.start_ticks = 0
        self.is_work = True
        self.kd = 2.5
        self.wait_time = 0.5


    def process(self, man):
        if self.is_work:
            if self.start_ticks != 0:
                self.preparing(man)
            elif self.if_stand(man):
                self.start_ticks = pygame.time.get_ticks()
        elif (pygame.time.get_ticks() - self.start_ticks)/1000 >= self.kd:
            self.is_work = True
            self.start_ticks = 0



    def if_stand(self, man):
        if man.y + man.h == self.y and man.x >= self.x and man.x + man.w <= self.x + self.w:
            return True


    def preparing(self, man):
        if self.if_stand(man):
            if (pygame.time.get_ticks() - self.start_ticks)/1000 >= self.wait_time:
                self.start_ticks = 0
                self.teleportation(man)
        else:
            self.start_ticks = 0


    def teleportation(self, man):
        man.x = self.finx
        man.y = self.finy
        self.is_work = False
        self.start_ticks = pygame.time.get_ticks()
