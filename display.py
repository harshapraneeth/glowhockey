import pygame as pg
import random
import puck
import engine

length, height = 450, 800
pg.init()
screen = pg.display.set_mode((length, height))
pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)

#--------------create puck-----------------
p1 = puck.Player((100,600))
p2 = puck.Player((100,100))
p1.color = (0,0,255)
disc = puck.Puck((p1,p2))
e = engine.Engine((0,0,0,0),[p1,p2,disc])

#---------------------------------------------------------

clock = pg.time.Clock()
running, drag = True, False
while (running):
    screen.fill((0,0,0))

    #------------draw lines---------------

    pg.draw.line(screen,(255,0,0),(10,5),(10,395),10)
    pg.draw.line(screen,(255,255,0),(10,405),(10,795),10)
    pg.draw.line(screen,(0,255,0),(440,5),(440,395),10)
    pg.draw.line(screen,(0,0,255),(440,405),(440,795),10)
    pg.draw.circle(screen,(255,255,255),(225,0),50,1)
    pg.draw.circle(screen,(255,255,255),(225,0),45,1)
    pg.draw.circle(screen,(255,255,255),(225,800),50,1)
    pg.draw.circle(screen,(255,255,255),(225,800),45,1)
    pg.draw.line(screen,(255,0,0),(20,10),(170,10),10)
    pg.draw.line(screen,(255,255,0),(20,790),(170,790),10)
    pg.draw.line(screen,(0,255,0),(280,10),(430,10),10)
    pg.draw.line(screen,(0,0,255),(280,790),(430,790),10)
    pg.draw.line(screen,(255,255,255),(0,398),(450,398))
    pg.draw.line(screen,(255,255,255),(0,402),(450,402))
    pg.draw.circle(screen, (255, 255, 255), (225, 400), 75, 1)
    pg.draw.circle(screen, (255, 255, 255), (225, 400), 70, 1)

    p1pts = myfont.render(str(p1.points), False, (255, 0, 0))
    p2pts = myfont.render(str(p2.points), False, (255, 0, 0))
    screen.blit(p1pts, (30, 25))
    screen.blit(p2pts, (405, 730))

    #--------------------------------------------

    t = clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if p1.inside(event.pos): drag = True
        if event.type == pg.MOUSEBUTTONUP: drag = False
        if event.type == pg.MOUSEMOTION:
            if drag:
                mouse_x, mouse_y = event.pos
                if mouse_x>435-p1.radius: mouse_x=435-p1.radius
                if mouse_x<15+p1.radius: mouse_x=15+p1.radius
                if mouse_y>785-p1.radius: mouse_y=785-p1.radius
                if mouse_y<400: mouse_y=400
                p1.dx, p1.dy = mouse_x-p1.x, mouse_y-p1.y
                p1.x = mouse_x
                p1.y = mouse_y

    #-----------------------------------------

    if p2.xg==p2.x and p2.yg==p2.y:
        if random.choice([True, True, True, False]) or disc.y>400: pos = (random.randint(15+p2.radius,435-p2.radius),random.randint(15+p2.radius,400))
        else: pos = (disc.x, disc.y)
    p2.moveTo(pos)

    #----------------draw pucks--------------
    p1.draw(screen)
    p2.draw(screen)
    p2.update()
    disc.draw(screen)
    disc.update()
    e.detectCollisons()

    clock.tick(120)
    pg.display.update()