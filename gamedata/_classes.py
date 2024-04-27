from random import randint as rnd

class Movable:
    def __init__(t, p, **s):
        t.id = p.g.create_oval(103,103,111,111, outline="#7777FF", width=2)
        t.position = {"x":10, "y": 10}
        
    def move(t,p):
         x,y = rnd(-1,1), rnd(-1,1)
         p.g.move(t.id, x*10, y*10)