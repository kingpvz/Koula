import tkinter
from tkinter import messagebox
import _levels

class Program:
      def __init__(t, **s):
            t.s = s
            t.w = tkinter.Tk()
            t.w.title("KOULA beta0.1")
            t.w.iconbitmap("_favicon.ico")
            t.g = tkinter.Canvas(bg=s["bg"],width=400,height=525)
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
            t.id = t.g.create_oval(203,203,211,211, fill=s["oval"]["fill"],outline=s["oval"]["outline"])
            t.colission = {"xl":200, "xr":210, "yt":210, "yb": 200}
            
            t.data = {"pts": 0, "level": s["level"]-1}
            
            t.object = {}
            t.object["line"] = t.g.create_line(0, 405, 405, 405, fill=s["objects"]["line"])
            t.object["counterText"] = t.g.create_text(10, 415, anchor="nw", text="Points:", font="arial 20", fill=s["objects"]["text"])
            t.object["counter"] = t.g.create_text(95, 415, anchor="nw", text="0 / 1", font="arial 20", fill=s["objects"]["text"])
            t.object["levelText"] = t.g.create_text(10, 450, anchor="nw", text="Level:", font="arial 20", fill=s["objects"]["text"])
            t.object["level"] = t.g.create_text(95, 450, anchor="nw", text="1", font="arial 20", fill=s["objects"]["text"])
            t.object["helpText"] = t.g.create_text(10, 490, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="Key Binds:")
            t.object["help"] = t.g.create_text(80, 490, anchor="nw", font="arial 10", fill=s["objects"]["text"], text="R = Restart, S = Skip Level, A = Previous Level\n\
Arrow Keys = Move, H = Help")
            
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
            for i in range(len(t.leveldata["pos"]["m"])):
                if t.colide(t.leveldata["pos"]["m"][i], (t.colission["xl"],t.colission["xr"],t.colission["yt"],t.colission["yb"])):
                    t.leveldata["pos"]["m"][i] = (-1, -1, -1, -1)
                    t.g.delete(t.leveldata["ovalm"][i])
                    t.cup()
          except KeyError: pass
          for i in range(len(t.leveldata["pos"]["c"])):
              try:
                if t.colide(t.leveldata["pos"]["c"][i], (t.colission["xl"],t.colission["xr"],t.colission["yt"],t.colission["yb"])):
                    t.leveldata["pos"]["c"][i] = (-1, -1, -1, -1)
                    t.g.delete(t.leveldata["ovalc"][i])
                    t.cdn()
              except KeyError: pass
                  
      def deleteall(t):
           for i in range(len(t.leveldata["pos"]["m"])): t.g.delete(t.leveldata["ovalm"][i])
           for i in range(len(t.leveldata["pos"]["c"])): t.g.delete(t.leveldata["ovalc"][i])
           t.leveldata = {}
                  
      def cup(t,b=1):
            t.data["pts"] += b
            t.scorer()
      def cdn(t,b=1):
            t.data["pts"] -= b
            t.scorer()
      def scorer(t):
            t.g.itemconfig(t.object["counter"], text=str(t.data["pts"])+" / "+str(t.leveldata["b"]))
            if t.data["pts"] == t.leveldata["b"]:
                 t.deleteall()
                 t.newLevel()
      
      def newLevel(t):
          t.data["level"]+=1
          t.leveldata = _levels.getLevel(t.data["level"], t)
          t.g.moveto(t.id, 202, 202)
          t.colission = {"xl":200, "xr":210, "yt":210, "yb": 200}
          t.g.itemconfig(t.object["level"], text=t.data["level"])
          t.data["pts"] = 0
          t.g.itemconfig(t.object["counter"], text=str(t.data["pts"])+" / "+str(t.leveldata["b"]))
          
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
          messagebox.showinfo("Help", _levels.HELP)
                  

p = Program(bg="#222222", oval={"fill":"yellow","outline":"yellow"}, objects={"line": "white", "text": "white"}, level=1)
input()
