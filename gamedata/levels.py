from random import randint as rnd
import gamedata._leveldata as _leveldata
import re
import gamedata._classes as CLASS

DATA = ["datastorage", {"blue": 1, "pts": 1}, {"pts": 7, "pos": (22,22), "data": _leveldata.lv2}, {"blue": 5, "black": 3, "pts": 4, "pos": (10,17)}, {"blue": 3, "black": 20, "pts": 3},\
       {"blue": 7, "black": 55, "pts": 6, "pos": (3,10)}, {"mblue": 3, "pts": 7, "pos":(1,5)}, {"data":_leveldata.lv7, "pts": 6, "pos": (20,2)}]

VALIDVALUES = r'^(blue|black|mblue\(\d+\)|mblue|mred|mred\(\d+\))$'
VALIDIDS = {"blue":{}, "black": {}, "mblue": {}, "mred": {}}

def getLevel(id, t):
    if id<len(DATA) and id>=1:
        DATA[id] = repair(DATA[id])
        if checkRequiredData(DATA[id]):
            if 0<=DATA[id]["pos"][0]<=39 and 0<=DATA[id]["pos"][1]<=39:
                sets = set()
                sets.add((DATA[id]["pos"][0],DATA[id]["pos"][1]))
                tiles = createTile()
                data = {"pts": DATA[id]["pts"], "ids":VALIDIDS, "tile":tiles, "pos":(DATA[id]["pos"][0],DATA[id]["pos"][1])}
                data["tile"][DATA[id]["pos"][0]][DATA[id]["pos"][1]]["data"] = "player"
                if "data" in DATA[id]:
                    DATA[id]["blue"], DATA[id]["black"], DATA[id]["mblue"] = 0,0,0
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
                for i in range(DATA[id]["mblue"]):
                    while True:
                        x,y = rnd(0,39),rnd(0,39)
                        if not (x,y) in sets: break
                    data["ids"]["mblue"][i] = CLASS.Movable(t, x, y, color="#7777FF", speed=10, type="blue")
                    data["tile"][x][y]["data"] = "mblue"
                    data["tile"][x][y]["id"] = i
                for i in range(DATA[id]["mred"]):
                    while True:
                        x,y = rnd(0,39),rnd(0,39)
                        if not (x,y) in sets: break
                    data["ids"]["mred"][i] = CLASS.Movable(t, x, y, color="#FF2222", speed=10, type="red")
                    data["tile"][x][y]["data"] = "mred"
                    data["tile"][x][y]["id"] = i
                return data
            else:
                tiles = createTile()
                tiles[20][20]["data"] = "player"
                return {"pts": 99999, "ids":VALIDIDS, "tile":tiles, "pos": (20,20)}
        else:
            tiles = createTile()
            tiles[20][20]["data"] = "player"
            return {"pts": 99999, "ids":VALIDIDS, "tile":tiles, "pos": (20,20)}
    else:
        tiles = createTile()
        tiles[20][20]["data"] = "player"
        return {"pts": 99999, "ids":VALIDIDS, "tile":tiles, "pos": (20,20)}
        

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
    if "blue" not in x: d["blue"] = 0
    if "black" not in x: d["black"] = 0
    if "pos" not in x: d["pos"] = (20, 20)
    if "mblue" not in x: d["mblue"] = 0
    if "mred" not in x: d["mred"] = 0
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
        if cmd[0] == "put":
            try:
                if len(cmd) != 5: raise ValueError("Fatal Syntax Error at line "+str(id+1))
                if not cmd[3].isdigit(): raise ValueError("X coordinate at line "+str(id+1)+" is not valid.")
                if not cmd[4].isdigit(): raise ValueError("Y coordinate at line "+str(id+1)+" is not valid.")
                if cmd[2] != "at": raise ValueError("'at' separator omited at line "+str(id+1))
            except ValueError as e:
                print(e)
                break
            else:
                try:
                    if not 0<=int(cmd[3])<=39: raise ValueError("X coordinate is out of bounds at line "+str(id+1))
                    if not 0<=int(cmd[4])<=39: raise ValueError("Y coordinate is out of bounds at line "+str(id+1))
                    if (int(cmd[3]), int(cmd[4])) in sets: raise ValueError("Line "+str(id+1)+" placement is already occupied.")
                    if not re.match(VALIDVALUES, cmd[1]): raise ValueError("Can't put "+cmd[1]+" into the level as it doesn't exist. Faulty line: "+str(id+1))
                    if "(" in cmd[1] and ")" not in cmd[1]: raise ValueError("Closing parenthesis omitted on line "+str(id+1))
                    if "(" in cmd[1] and not cmd[1][cmd[1].find("(")+1:cmd[1].find(")")].isdigit(): raise ValueError("Incorrect parameter on line "+str(id+1))
                except ValueError as e:
                    print(e)
                    break
                else:
                    if "(" in cmd[1]: param = int(cmd[1][cmd[1].find("(")+1:cmd[1].find(")")]); cmd[1] = cmd[1][:cmd[1].find("(")]
                    else: param = None
                    tiles[int(cmd[3])][int(cmd[4])]["data"] = cmd[1]
                    tiles[int(cmd[3])][int(cmd[4])]["id"] = id
                    sets.add((int(cmd[3]),int(cmd[4])))
                    if cmd[1] == "blue": ids[cmd[1]][id] = t.g.create_oval(int(cmd[3])*10+3,int(cmd[4])*10+3,int(cmd[3])*10+11,int(cmd[4])*10+11, fill="blue", outline="white")
                    if cmd[1] == "black": ids[cmd[1]][id] = t.g.create_oval(int(cmd[3])*10+3,int(cmd[4])*10+3,int(cmd[3])*10+11,int(cmd[4])*10+11, fill="black", outline="red")
                    if cmd[1] == "mblue":
                        if param: rpid = param
                        else: rpid = 10
                        ids[cmd[1]][id] = CLASS.Movable(t, int(cmd[3]), int(cmd[4]), color="#7777FF", speed=rpid, type="blue")
                    if cmd[1] == "mred":
                        if param: rpid = param
                        else: rpid = 10
                        ids[cmd[1]][id] = CLASS.Movable(t, int(cmd[3]), int(cmd[4]), color="#FF2222", speed=rpid, type="red")
        else: print("Command at line", id+1, "doesn't exist.")
    return ids,tiles
        
                    
                    