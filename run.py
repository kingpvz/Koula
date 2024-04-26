import tkinter
from tkinter import messagebox
import _levels, _info

class Movable:
    def __init__(t, p, **s):
        t.m = p.g.create_oval(103,103,111,111, fill="#222222", outline="blue", width=3)

class Program:
      def __init__(t, **s):
            t.s = s
            t.w = tkinter.Tk()
            t.w.title("KOULA "+_info.VERSION)
            t.w.iconbitmap("_favicon.ico")
            t.g = tkinter.Canvas(bg=s["bg"],width=400,height=525,cursor="dot")
            t.dx = 0
            t.dy = 0
            t.g.pack()
            t.g.bind_all('<Left>', t.vlavo)
            t.g.bind_all('<Right>', t.vpravo)
            t.g.bind_all('<Up>', t.nahor)
            t.g.bind_all('<Down>', t.dole)
            t.g.bind_all('s', t.skipLevel)
            t.g.bind_all('a', t.previousLevel)
            t.g.bind_all('r', t.restartLevel)
            t.g.bind_all('h', t.showHelp)
            t.g.bind_all('c', t.showChangelog)
            t.id = t.g.create_oval(203,203,211,211, fill=s["oval"]["fill"],outline=s["oval"]["outline"])
            
            t.data = {"pts": 0, "level": s["level"]-1}
            
            t.object = {}
            t.object["line"] = t.g.create_line(0, 405, 405, 405, fill=s["objects"]["line"])
            t.object["counterText"] = t.g.create_text(10, 415, anchor="nw", text="Points:", font="arial 20", fill=s["objects"]["text"])
            t.object["counter"] = t.g.create_text(95, 415, anchor="nw", text="0 / 1", font="arial 20", fill=s["objects"]["text"])
            t.object["levelText"] = t.g.create_text(10, 450, anchor="nw", text="Level:", font="arial 20", fill=s["objects"]["text"])
            t.object["level"] = t.g.create_text(95, 450, anchor="nw", text="1", font="arial 20", fill=s["objects"]["text"])
            t.object["helpText"] = t.g.create_text(10, 490, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="Key Binds:")
            t.object["help"] = t.g.create_text(80, 490, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="R = Restart, S = Skip Level, A = Previous Level\n\
Arrow Keys = Move, H = Help, C = Changelog")
            
            t.newLevel()

      def hni(t):
            t.colission["xl"]+=t.dx; t.colission["xr"]+=t.dx; t.colission["yt"]+=t.dy; t.colission["yb"]+=t.dy
            t.g.move(t.id, t.dx, t.dy)
            t.dx = 0
            t.dy = 0
            t.getTouch()
      def vlavo(t,e):
            if not t.colission["xl"]<=0:
                  t.dx=-10
            t.hni()            
      def vpravo(t,e):
            if not t.colission["xr"]>=400:
                  t.dx = 10
            t.hni()
      def nahor(t,e):
            if not t.colission["yb"]<=0:
                  t.dy = -10
            t.hni()
      def dole(t,e):
            if not t.colission["yt"]>=400:
                  t.dy = 10
            t.hni()
            
      def colide(t, pos1, pos2):
            if pos2[0]>=pos1[0] and pos2[1]<=pos1[1] and pos2[2]>=pos1[2] and pos2[3]<=pos1[3]: return True
            else: return False
      def getTouch(t):
          try:
            for i in range(len(t.leveldata["pos"]["blue"])):
                if t.colide(t.leveldata["pos"]["blue"][i], (t.colission["xl"],t.colission["xr"],t.colission["yt"],t.colission["yb"])):
                    t.leveldata["pos"]["blue"][i] = (-1, -1, -1, -1)
                    t.g.delete(t.leveldata["ovalblue"][i])
                    t.cup()
          except KeyError: pass
          for i in range(len(t.leveldata["pos"]["black"])):
              try:
                if t.colide(t.leveldata["pos"]["black"][i], (t.colission["xl"],t.colission["xr"],t.colission["yt"],t.colission["yb"])):
                    t.leveldata["pos"]["black"][i] = (-1, -1, -1, -1)
                    t.g.delete(t.leveldata["ovalblack"][i])
                    t.cdn()
              except KeyError: pass
                  
      def deleteall(t):
           for i in range(len(t.leveldata["pos"]["blue"])): t.g.delete(t.leveldata["ovalblue"][i])
           for i in range(len(t.leveldata["pos"]["black"])): t.g.delete(t.leveldata["ovalblack"][i])
           t.leveldata = {}
                  
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
                 t.newLevel()
      
      def newLevel(t):
          t.data["level"]+=1
          t.leveldata = _levels.getLevel(t.data["level"], t)
          t.g.moveto(t.id, t.leveldata["dpos"][0]+2, t.leveldata["dpos"][1]+2)
          t.colission = {"xl":t.leveldata["dpos"][0], "xr":t.leveldata["dpos"][0]+10, "yt":t.leveldata["dpos"][1]+10, "yb": t.leveldata["dpos"][1]}
          t.g.itemconfig(t.object["level"], text=t.data["level"])
          t.data["pts"] = 0
          t.g.itemconfig(t.object["counter"], text=str(t.data["pts"])+" / "+str(t.leveldata["pts"]))
          t.leveldata["MOVING"] = "a"
          
      def skipLevel(t,e):
           t.deleteall()
           t.newLevel()
      def previousLevel(t,e):
          t.deleteall()
          t.data["level"] -= 2
          t.newLevel()
      def restartLevel(t,e):
          t.deleteall()
          t.data["level"] -= 1
          t.newLevel()
          
      def showHelp(t,e):
          messagebox.showinfo("Help", _info.HELP)
      def showChangelog(t,e):
          messagebox.showinfo("Changelog", _info.CHANGELOG)
                  

p = Program(bg="#222222", oval={"fill":"yellow","outline":"yellow"}, objects={"line": "white", "text": "white"}, level=1)
print("If you are running this in IDLE, press the ENTER key on your keyboard to run the program.")
input()