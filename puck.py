import pygame as pg
import math

class Player:
    def __init__(self,position):
        self.radius = 30
        self.x, self.y = position
        self.xg, self.yg = self.x, self.y
        self.mass = 10
        self.points = 0
        self.dx, self.dy = 0, 0
        self.color = (255,0,0)
    def draw(self,screen):
        pg.draw.circle(screen,self.color,(self.x, self.y),self.radius,15)
    def inside(self,position):
        if position[0]>=self.x-self.radius and position[0]<=self.x+self.radius:
            if position[1]>=self.y-self.radius and position[1]<=self.y+self.radius: return True
        return False
    def moveTo(self,position):
        self.dx, self.dy = 0, 0
        self.xg, self.yg = position
        if self.xg>self.x:
            self.dx = 1
            if self.xg-self.x>5: self.dx=5
            if self.xg-self.x>10: self.dx=10
            if self.xg-self.x>20: self.dx=20
            if self.xg-self.x>30: self.dx=30
        if self.xg<self.x:
            self.dx = -1
            if self.x-self.xg>5: self.dx=-5
            if self.x-self.xg>10: self.dx=-10
            if self.x-self.xg>20: self.dx=-20
            if self.x-self.xg>30: self.dx=-30
        if self.yg>self.y:
            self.dy = 1
            if self.yg-self.y>5: self.dy=5
            if self.yg-self.y>10: self.dy=10
            if self.yg-self.y>20: self.dy=20
            if self.yg-self.y>30: self.dy=30
        if self.yg < self.y:
            self.dy = -1
            if self.y - self.yg > 5: self.dy = -5
            if self.y - self.yg > 10: self.dy = -10
            if self.y - self.yg > 20: self.dy = -20
            if self.y - self.yg > 30: self.dy = -30
    def update(self):
        self.x += self.dx
        self.y += self.dy

class Puck:
    def __init__(self,players):
        self.radius = 20
        self.mass = 5
        self.p1, self.p2 = players
        self.x, self.y = (225,400)
        self.dx, self.dy = 0, 0
        self.color = (255,255,0)
    def draw(self,screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def update(self):
        if self.x >= 435 - self.radius:
            self.x = 435 - self.radius
            self.dx *= -1
        if self.x <= 15 + self.radius:
            self.x = 15 + self.radius
            self.dx *= -1
        if self.y >= 785 - self.radius:
            if 175<=self.x-self.radius and 275>=self.x+self.radius:
                if self.y >= 800-self.radius:
                    self.p2.points += 1
                    self.x, self.y = 225, 400
                    self.dx, self.dy = 0, 0
            else:
                self.y = 785 - self.radius
                self.dy *= -1
        if self.y <= 15 + self.radius:
            if 175 <= self.x - self.radius and 275 >= self.x + self.radius:
                if self.y <= self.radius:
                    self.p1.points += 1
                    self.x, self.y = 225, 400
                    self.dx, self.dy = 0, 0
            else:
                self.y = 15 + self.radius
                self.dy *= -1
        self.dx *= 0.95
        self.dy *= 0.95
        self.x = int(self.x+self.dx)
        self.y = int(self.y+self.dy)

