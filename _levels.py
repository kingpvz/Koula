from random import randint as rnd

DATA = ["datastorage", {"m": 1, "c": 0, "b": 1}, {"m": 10, "c": 0, "b": 10}, {"m": 10, "c": 3, "b": 8}, {"m": 5, "c": 10, "b": 5}, {"m": 10, "c": 50, "b": 9}]

HELP = """Welcome to KOULA!
(the best game ever for real)

This is a quick tutorial to help you get started.
Every level consists of many small balls on the screen. And the goal is simple: Get the amount of points you need to win the level.
Every ball has a different purpose and acts differently too.

Here is an overview:
YELLOW - Your player ball. You can move it around. Always spawns in the middle of the playarea.
BLUE (white outline) - Goal ball. Collect it to get 1 point.
BLACK (red outline) - Doom ball. Collect it to lose 1 point. Hopefully looks dangerous.

Levels will always give you at least the amount of points you need. Basically try not to lose any. Simple as that!
"""

def getLevel(id, t):
    if id<len(DATA) and id>=1:
        sets = set()
        sets.add((200,200))
        data = {"b": DATA[id]["b"], "ovalm":{}, "ovalc":{}, "pos":{"m":{}, "c":{}}}
        for i in range(DATA[id]["m"]):
            while True:
                x,y = 10*rnd(0,39),10*rnd(0,39)
                if not (x,y) in sets: break
            data["ovalm"][i] = t.g.create_oval(x+3,y+3,x+11,y+11, fill="blue", outline="white")
            data["pos"]["m"][i] = (x,x+10,y+10,y)
            sets.add((x,y))
        for i in range(DATA[id]["c"]):
            while True:
                x,y = 10*rnd(0,39),10*rnd(0,39)
                if not (x,y) in sets: break
            data["ovalc"][i] = t.g.create_oval(x+3,y+3,x+11,y+11, fill="black", outline="red")
            data["pos"]["c"][i] = (x,x+10,y+10,y)
            sets.add((x,y))
        print(sets)
        return data
    else:
        return {"b": 9999, "ovalm":{}, "ovalc":{}, "pos":{"m":{}, "c":{}}}
