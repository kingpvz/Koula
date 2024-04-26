from random import randint as rnd
import _leveldata
import re

DATA = ["datastorage", {"blue": 1, "pts": 1}, {"pts": 10, "pos": (22,22), "data": _leveldata.lv2}, {"blue": 10, "black": 3, "pts": 8, "pos": (10,17)}, {"blue": 5, "black": 10, "pts": 5},\
       {"blue": 10, "black": 50, "pts": 9, "pos": (3,10)}]

VALIDVALUES = {"blue", "black"}

def getLevel(id, t):
    if id<len(DATA) and id>=1:
        DATA[id] = repair(DATA[id])
        if checkRequiredData(DATA[id]):
            if 0<=DATA[id]["pos"][0]<=39 and 0<=DATA[id]["pos"][1]<=39:
                sets = set()
                sets.add((DATA[id]["pos"][0],DATA[id]["pos"][1]))
                tiles = createTile()
                data = {"pts": DATA[id]["pts"], "ids":{"blue":{}, "black": {}, "movable": {}}, "tile":tiles, "pos":(DATA[id]["pos"][0],DATA[id]["pos"][1])}
                data["tile"][DATA[id]["pos"][0]][DATA[id]["pos"][1]]["data"] = "player"
                if "data" in DATA[id]:
                    DATA[id]["blue"], DATA[id]["black"] = 0,0
                    data["ids"], data["tile"] = createLevel(data, DATA[id]["data"], DATA[id]["pos"], t)
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
        else:
            tiles = createTile()
            tiles[20][20]["data"] = "player"
            return {"pts": 99999, "ids":{"blue": {}, "black": {}, "movable":{}}, "tile":tiles, "pos": (20,20)}
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

def checkRequiredData(x):
    if "pts" not in x:
        return False
    return True

def repair(x):
    d = x
    if "blue" not in x:
        d["blue"] = 0
    if "black" not in x:
        d["black"] = 0
    if "pos" not in x:
        d["pos"] = (20, 20)
    return d

def createLevel(base, script, pos, t):
    tiles = base["tile"]
    ids = base["ids"]
    script = re.split(r"[;\n]+", script)
    script = [i.lower().strip() for i in script if i != ""]
    sets = set()
    sets.add(pos)
    
    for i in script:
        cmd = i.split()
        id = script.index(i)
        try:
            if len(cmd) != 5: raise SyntaxError(0)
            if cmd[0] != "at": raise SyntaxError(1)
            if not cmd[1].isdigit(): raise ValueError(0)
            if not cmd[2].isdigit(): raise ValueError(1)
            if cmd[3] != "put": raise SyntaxError(2)
        except SyntaxError as e:
            if e == 0: print("Fatal Syntax Error at line", id+1)
            if e == 1: print("Unknown Command at line", id+1)
            if e == 2: print("'put' separator omited at line", id+1)
            break
        except ValueError as e:
            if e == 0: print("X coordinate at line", id+1, "is not valid.")
            if e == 1: print("Y coordinate at line", id+1, "is not valid.")
            break
        else:
            try:
                if not 0<=int(cmd[1])<=39: raise ValueError(0)
                if not 0<=int(cmd[2])<=39: raise ValueError(1)
                if (int(cmd[1]), int(cmd[2])) in sets: raise ValueError(2)
            except ValueError as e:
                if e == 0: print("X coordinate is out of bounds at line", id+1)
                if e == 1: print("Y coordinate is out of bounds at line", id+1)
                if e == 2: print("Line", id+1, "placement is already occupied.")
                break
            else:
                try:
                    if cmd[4] not in VALIDVALUES: raise ValueError(0)
                except ValueError as e:
                    if e == 0: print("Can't put", cmd[4], "into the level as it doesn't exist. Faulty line:", id+1)
                    break
                else:
                    tiles[int(cmd[1])][int(cmd[2])]["data"] = cmd[4]
                    tiles[int(cmd[1])][int(cmd[2])]["id"] = id
                    sets.add((int(cmd[1]),int(cmd[2])))
                    if cmd[4] == "blue": ids[cmd[4]][id] = t.g.create_oval(int(cmd[1])*10+3,int(cmd[2])*10+3,int(cmd[1])*10+11,int(cmd[2])*10+11, fill="blue", outline="white")
                    if cmd[4] == "black": ids[cmd[4]][id] = t.g.create_oval(int(cmd[1])*10+3,int(cmd[2])*10+3,int(cmd[1])*10+11,int(cmd[2])*10+11, fill="black", outline="red")
    return ids,tiles
        
                    
                    