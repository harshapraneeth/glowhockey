import math

class Engine:
    def __init__(self, bounds, objects):
        self.xmin, self.xmax, self.ymin, self.ymax = bounds
        self.objs = objects
    def collision(self, a, b):
        if True:
            d = a.radius+b.radius-self.distance((a.x,a.y),(b.x,b.y))
            if d==0: return True
            if d>0:
                if b.mass > a.mass:
                    if a.x < b.x: a.x -= int(d / 2)
                    else: a.x += int(d / 2)
                    if a.y < b.y: a.y -= int(d / 2)
                    else: a.y += int(d / 2)
                else:
                    if b.x < a.x: b.x -= int(d / 2)
                    else: b.x += int(d / 2)
                    if b.y < a.y: b.y -= int(d / 2)
                    else: b.y += int(d / 2)
                return True
        return False
    def distance(self,p1,p2):
        return math.sqrt(math.pow((p1[0]-p2[0]),2)+math.pow((p1[1]-p2[1]),2))
    def detectCollisons(self):
        n = len(self.objs)
        for i in range(n):
            for j in range(i):
                if not self.collision(self.objs[i], self.objs[j]): continue
                self.objs[i].dx *= 0.9
                self.objs[i].dy *= 0.9
                self.objs[j].dx *= 0.9
                self.objs[j].dy *= 0.9
                tempx = self.objs[i].dx
                self.objs[i].dx = ((self.objs[i].mass - self.objs[j].mass) / (
                        self.objs[i].mass + self.objs[j].mass)) * self.objs[i].dx + 2 * (
                                         self.objs[j].mass / (
                                         self.objs[i].mass + self.objs[j].mass)) * \
                                 self.objs[j].dx
                self.objs[j].dx = 2 * (
                        self.objs[i].mass / (self.objs[i].mass + self.objs[j].mass)) * tempx + (
                                         (self.objs[j].mass - self.objs[i].mass) / (
                                         self.objs[i].mass + self.objs[j].mass)) * \
                                 self.objs[j].dx
                tempy = self.objs[i].dy
                self.objs[i].dy = ((self.objs[i].mass - self.objs[j].mass) / (
                        self.objs[i].mass + self.objs[j].mass)) * self.objs[i].dy + 2 * (
                                          self.objs[j].mass / (
                                          self.objs[i].mass + self.objs[j].mass)) * \
                                  self.objs[j].dy
                self.objs[j].dy = 2 * (
                        self.objs[i].mass / (self.objs[i].mass + self.objs[j].mass)) * tempy + (
                                          (self.objs[j].mass - self.objs[i].mass) / (
                                          self.objs[i].mass + self.objs[j].mass)) * \
                                  self.objs[j].dy

