from random import randint as rnd

DATA = ["datastorage", {"blue": 1, "black": 0, "pts": 1, "pos": (20,20)}, {"blue": 10, "black": 0, "pts": 10, "pos": (22,22)}, {"blue": 10, "black": 3, "pts": 8, "pos": (10,17)}, {"blue": 5, "black": 10, "pts": 5, "pos": (20,20)},\
       {"blue": 10, "black": 50, "pts": 9, "pos": (3,10)}]

def getLevel(id, t):
    if id<len(DATA) and id>=1 and 0<=DATA[id]["pos"][0]<=39 and 0<=DATA[id]["pos"][1]<=39:
        sets = set()
        sets.add((DATA[id]["pos"][0],DATA[id]["pos"][1]))
        tiles = createTile()
        data = {"pts": DATA[id]["pts"], "ids":{"blue":{}, "black": {}, "movable": {}}, "tile":tiles, "pos":(DATA[id]["pos"][0],DATA[id]["pos"][1])}
        data["tile"][DATA[id]["pos"][0]][DATA[id]["pos"][1]]["data"] = "player"
        for i in range(DATA[id]["blue"]):
            while True:
                x,y = rnd(0,39),rnd(0,39)
                if not (x,y) in sets: break
            data["ids"]["blue"][i] = t.g.create_oval(x*10+3,y*10+3,x*10+11,y*10+11, fill="blue", outline="white")
            data["tile"][x][y]["data"] = "blue"
            data["tile"][x][y]["id"] = i
            sets.add((x,y))
        for i in range(DATA[id]["black"]):
            while True:
                x,y = rnd(0,39),rnd(0,39)
                if not (x,y) in sets: break
            data["ids"]["black"][i] = t.g.create_oval(x*10+3,y*10+3,x*10+11,y*10+11, fill="black", outline="red")
            data["tile"][x][y]["data"] = "black"
            data["tile"][x][y]["id"] = i
            sets.add((x,y))
        return data
    else:
        tiles = createTile()
        tiles[20][20]["data"] = "player"
        return {"pts": 99999, "ids":{"blue": {}, "black": {}, "movable":{}}, "tile":tiles, "pos": (20,20)}

def createTile():
    df = []
    for i in range(40):
        row = []
        for j in range(40):
            row.append({"data": "empty", "id": -1})
        df.append(row)
    return df