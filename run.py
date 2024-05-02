import tkinter
from tkinter import messagebox
import gamedata.levels as _levels
import gamedata._info as _info
from gamedata._classes import *
import gamedata._messages as _messages

class Program:
      def __init__(t, **s):
            t.s = s
            t.w = tkinter.Tk()
            t.w.title("KOULA "+_info.VERSION)
            t.w.iconbitmap("gamedata/other/_favicon.ico")
            t.w.config(cursor="none")
            t.g = tkinter.Canvas(bg=s["bg"],width=400,height=535,cursor="none")
            
            t.dx = 0
            t.dy = 0
            t.g.pack()
            t.id = t.g.create_oval(203,203,211,211, fill="yellow",outline="yellow")
            
            t.g.bind_all('<Left>', t.vlavo)
            t.g.bind_all('<Right>', t.vpravo)
            t.g.bind_all('<Up>', t.nahor)
            t.g.bind_all('<Down>', t.dole)
            t.g.bind_all('a', t.vlavo)
            t.g.bind_all('d', t.vpravo)
            t.g.bind_all('w', t.nahor)
            t.g.bind_all('s', t.dole)
            t.g.bind_all('e', t.skipLevel)
            t.g.bind_all('q', t.previousLevel)
            t.g.bind_all('r', t.restartLevel)
            t.g.bind_all('h', t.showHelp)
            t.g.bind_all('c', t.showChangelog)
            
            t.data = {"pts": 0, "level": s["level"]-1, "backlevel": 0}
            
            t.object = {}
            t.object["line"] = t.g.create_line(0, 405, 405, 405, fill=s["objects"]["line"])
            t.object["counterText"] = t.g.create_text(10, 415, anchor="nw", text="Points:", font="arial 20", fill=s["objects"]["text"])
            t.object["counter"] = t.g.create_text(95, 415, anchor="nw", text="0 / 1", font="arial 20", fill=s["objects"]["text"])
            t.object["levelText"] = t.g.create_text(10, 450, anchor="nw", text="Level:", font="arial 20", fill=s["objects"]["text"])
            t.object["level"] = t.g.create_text(95, 450, anchor="nw", text="1", font="arial 20", fill=s["objects"]["text"])
            t.object["helpText"] = t.g.create_text(10, 485, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="Key Binds:")
            t.object["help"] = t.g.create_text(80, 485, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="H = Controls and Help, C = Changelog")
            t.object["message"] = t.g.create_text(200,505, anchor="n", text="...", font="bahnschrift 13", fill=s["objects"]["text"])
            
            t.msg(_messages.randomMessage())
            t.newLevel()

      def hni(t):
            t.leveldata["tile"][t.position["x"]][t.position["y"]]["data"] = "empty"
            t.position["x"]+=t.dx; t.position["y"]+=t.dy
            t.g.move(t.id, t.dx*10, t.dy*10)
            t.dx = 0
            t.dy = 0
            t.touch((t.position["x"], t.position["y"]))
            t.leveldata["tile"][t.position["x"]][t.position["y"]]["data"] = "player"
                
      def vlavo(t,e):
            if not t.position["x"]<=0:
                  t.dx = -1
            t.hni()            
      def vpravo(t,e):
            if not t.position["x"]>=39:
                  t.dx = 1
            t.hni()
      def nahor(t,e):
            if not t.position["y"]<=0:
                  t.dy = -1
            t.hni()
      def dole(t,e):
            if not t.position["y"]>=39:
                  t.dy = 1
            t.hni()
            
      def getObj(t, x, y):
            return t.leveldata["tile"][x][y]
      def touch(t, pos):
          try:
            tileobj = t.getObj(pos[0], pos[1])
            if not tileobj["data"] == "empty":
                 if tileobj["data"] == "blue":
                     tileobj["data"] = "empty"
                     t.g.delete(t.leveldata["ids"]["blue"][tileobj["id"]])
                     t.cup()
                 if tileobj["data"] == "black":
                     tileobj["data"] = "empty"
                     t.g.delete(t.leveldata["ids"]["black"][tileobj["id"]])
                     t.cdn()
                 if tileobj["data"] == "mblue":
                     t.leveldata["ids"]["mblue"][tileobj["id"]].collide()
                     tileobj["data"] = "empty"
                     t.cup(3)
                 if tileobj["data"] == "mred":
                     t.leveldata["ids"]["mred"][tileobj["id"]].collide()
                     tileobj["data"] = "empty"
                     t.cdn(3)
          except KeyError: pass
                  
      def cup(t,b=1):
            t.data["pts"] += b
            t.scorer()
      def cdn(t,b=1):
            t.data["pts"] -= b
            t.scorer()
      def scorer(t):
            t.g.itemconfig(t.object["counter"], text=str(t.data["pts"])+" / "+str(t.leveldata["pts"]))
            if t.data["pts"] >= t.leveldata["pts"]:
                 t.deleteall()
                 t.msg("Great job on beating level "+str(t.data["level"]))
                 t.newLevel()
      
      def newLevel(t):
          t.data["level"]+=1
          t.leveldata = _levels.getLevel(t.data["level"], t)
          t.g.moveto(t.id, t.leveldata["pos"][0]*10+2, t.leveldata["pos"][1]*10+2)
          t.position = {"x":t.leveldata["pos"][0], "y":t.leveldata["pos"][1]}
          t.g.itemconfig(t.object["level"], text=t.data["level"])
          t.data["pts"] = 0
          t.g.itemconfig(t.object["counter"], text=str(t.data["pts"])+" / "+str(t.leveldata["pts"]))
          for i in t.leveldata["ids"]["mblue"]: t.leveldata["ids"]["mblue"][i].repetition()
          for i in t.leveldata["ids"]["mred"]: t.leveldata["ids"]["mred"][i].repetition()
      def deleteall(t):
           for i in t.leveldata["ids"]["blue"]: t.g.delete(t.leveldata["ids"]["blue"][i])
           for i in t.leveldata["ids"]["black"]: t.g.delete(t.leveldata["ids"]["black"][i])
           for i in t.leveldata["ids"]["mblue"]: t.leveldata["ids"]["mblue"][i].collide()
           for i in t.leveldata["ids"]["mred"]: t.leveldata["ids"]["mred"][i].collide()
           t.leveldata = {}
          
      def skipLevel(t,e):
           t.deleteall()
           t.newLevel()
           t.data["backlevel"] = 0
           t.msg("Level skipped!")
      def previousLevel(t,e):
          if t.data["level"] > 1:
            t.deleteall()
            t.data["level"] -= 2
            t.newLevel()
            t.data["backlevel"] = 0
            t.msg("Previous level loaded!")
          else:
              t.data["backlevel"] += 1
              t.msg(_messages.getLevelBack(t.data["backlevel"]))
      def restartLevel(t,e):
          t.deleteall()
          t.data["level"] -= 1
          t.newLevel()
          t.msg("Level restarted!")
          t.data["backlevel"] = 0
          
      def showHelp(t,e):
          messagebox.showinfo("Help", _info.HELP)
      def showChangelog(t,e):
          messagebox.showinfo("Changelog", _info.CHANGELOG)
      
      def msg(t, txt):
          t.g.itemconfig(t.object["message"], text=txt)

p = Program(bg="#222222", objects={"line": "white", "text": "white"}, level=1)
print("If you are running this in IDLE, press the ENTER key on your keyboard to run the program.")
input()