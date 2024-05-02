from random import randint as rnd

class Movable:
    def __init__(t, p, x, y, **s):
        t.id = p.g.create_oval((x*10)+3,(y*10)+3,(x*10)+11,(y*10)+11, outline=s["color"], width=2)
        t.position = {"x":x, "y": y}
        t.exists = True
        t.p = p
        t.spd = s["speed"]
        t.type = s["type"]
        
    def move(t):
         x,y = rnd(-1,1), rnd(-1,1)
         if t.position["x"]<=0 and x==-1:x=1
         if t.position["x"]>=39 and x==1:x=-1
         if t.position["y"]<=0 and y==-1:y=1
         if t.position["y"]>=39 and y==1:y=-1
         if t.position["x"]+x>=0 and t.position["x"]+x<=39 and t.position["y"]+y>=0 and t.position["y"]+y<=39:
             if t.p.getObj(t.position["x"]+x, t.position["y"]+y)["data"] == "empty":
                 t.p.g.move(t.id, x*10, y*10)
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["data"] = "empty"
                 rid = t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["id"]
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["id"] = -1
                 t.position["x"] += x; t.position["y"] += y
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["data"] = "m"+t.type
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["id"] = rid
             elif t.p.getObj(t.position["x"]+x, t.position["y"]+y)["data"] == "player":
                 t.p.touch((t.position["x"], t.position["y"]))
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["data"] = "empty"
                 t.p.leveldata["tile"][t.position["x"]][t.position["y"]]["id"] = -1

    def collide(t):
        t.p.g.delete(t.id)
        t.exists = False
        
    def repetition(t):
        if t.exists:
            t.move()
            t.p.g.after(int(1000/t.spd), t.repetition)