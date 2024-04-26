from random import randint as rnd

DATA = ["datastorage", {"blue": 1, "black": 0, "pts": 1, "dpos": (20,20)}, {"blue": 10, "black": 0, "pts": 10, "dpos": (22,22)}, {"blue": 10, "black": 3, "pts": 8, "dpos": (10,17)}, {"blue": 5, "black": 10, "pts": 5, "dpos": (20,20)},\
       {"blue": 10, "black": 50, "pts": 9, "dpos": (3,10)}]

def getLevel(id, t):
    if id<len(DATA) and id>=1 and 0<=DATA[id]["dpos"][0]<=39 and 0<=DATA[id]["dpos"][1]<=39:
        sets = set()
        sets.add((DATA[id]["dpos"][0]*10,DATA[id]["dpos"][1]*10))
        data = {"pts": DATA[id]["pts"], "ovalblue":{}, "ovalblack":{}, "pos":{"blue":{}, "black":{}}, "dpos": (DATA[id]["dpos"][0]*10,DATA[id]["dpos"][1]*10)}
        for i in range(DATA[id]["blue"]):
            while True:
                x,y = 10*rnd(0,39),10*rnd(0,39)
                if not (x,y) in sets: break
            data["ovalblue"][i] = t.g.create_oval(x+3,y+3,x+11,y+11, fill="blue", outline="white")
            data["pos"]["blue"][i] = (x,x+10,y+10,y)
            sets.add((x,y))
        for i in range(DATA[id]["black"]):
            while True:
                x,y = 10*rnd(0,39),10*rnd(0,39)
                if not (x,y) in sets: break
            data["ovalblack"][i] = t.g.create_oval(x+3,y+3,x+11,y+11, fill="black", outline="red")
            data["pos"]["black"][i] = (x,x+10,y+10,y)
            sets.add((x,y))
        return data
    else:
        return {"pts": 9999, "ovalblue":{}, "ovalblack":{}, "pos":{"blue":{}, "black":{}}, "dpos": (200, 200)}
