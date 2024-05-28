import tkinter
from tkinter import messagebox
import gamedata._info as _info

class Editor:
    def __init__(t, rootWindow):
        t.w = tkinter.Toplevel()
        t.w.title("KOULA LEVEL EDITOR")
        t.w.iconbitmap("gamedata/other/_favicon.ico")
        t.w.config(cursor="none")
        t.g = tkinter.Canvas(t.w, bg="#222222",width=400,height=535,cursor="plus")
        t.g.pack()
        t.rootWindow = rootWindow
        t.w.protocol("WM_DELETE_WINDOW", t.restoreOnDeath)
        t.w.resizable(0,0)

        t.data = {"chosenBall": "blue", "playerExists": False, "playerPos": (-1,-1)}

        t.object = {}
        t.object["line"] = t.g.create_line(0, 405, 405, 405, fill="white")
        t.object["ballText"] = t.g.create_text(10, 410, anchor="nw", fill="white", text="Ball:", font="arial 15")
        t.object["ballChooser"] = t.g.create_rectangle(77, 414, 93, 430, outline="#dddd88")
        
        t.object["buttonControls"] = t.g.create_rectangle(160,465,240,485, fill="#cccccc", outline="#000000")
        t.object["buttonControlsText"] = t.g.create_text(200,474, text="CONTROLS", font="ubuntu 10 bold", fill="black")
        t.g.tag_bind(t.object["buttonControls"], '<ButtonPress-1>', t.showHelp)
        t.g.tag_bind(t.object["buttonControlsText"], '<ButtonPress-1>', t.showHelp)
        
        t.object["ballPlayer"] = t.g.create_oval(60, 417, 70, 427, fill="yellow", outline="yellow", tags="ballchoice_player")
        t.object["ballBlue"] = t.g.create_oval(80, 417, 90, 427, fill="blue", outline="white", tags="ballchoice_blue")
        t.object["ballBlack"] = t.g.create_oval(100, 417, 110, 427, fill="black", outline="red", tags="ballchoice_black")
        t.object["ballMblue"] = t.g.create_oval(120, 417, 130, 427, fill="#222222", outline="#7777FF", width=2, tags="ballchoice_mblue")
        t.object["ballMred"] = t.g.create_oval(140, 417, 150, 427, fill="#222222", outline="#FF2222", width=2, tags="ballchoice_mred")
        
        t.object["speedinputwidget"] = tkinter.Entry(t.g, background="#444444", fg="white", font="arial 12", bd=2, width=5, textvariable=tkinter.IntVar(t.w, 10), justify="center")
        t.object["speedinput"] = t.g.create_window(340,410,window=t.object["speedinputwidget"],anchor="nw")
        t.object["speedtext"] = t.g.create_text(365, 442, fill="white", text="SPEED", font="arial 8")
        
        t.object["message"] = t.g.create_text(200,510, anchor="n", text="...", font="ubuntu 12 bold", fill="white")
        
        t.dump = set()

        t.griddata = []
        for i in range(40):
            row = []
            for j in range(40):
                row.append({"data": "empty", "id": -1, "speed": 0})
            t.griddata.append(row)

        t.grid = []
        for i in range(40):
            row = []
            for j in range(40):
                row.append(t.g.create_rectangle(j*10+3,i*10+3,j*10+11,i*10+11, tags=str(j)+";"+str(i), width=0))
            t.grid.append(row)

        t.g.bind_all('<ButtonPress-1>', t.clickLeft)
        t.g.bind_all('<ButtonPress-3>', t.clickRight)
        
        t.msg("Info will show here.")
        
    def clickLeft(t,e): 
        R = t.g.gettags("current")
        if t.validateSpeed():
            if len(R) == 2 and R[0] != "current" and "ballchoice" not in R[0]:
                X,Y = map(int, R[0].split(";"))
                
                if (X,Y) in t.dump:
                    t.clickRight(None)
                    
                if t.data["chosenBall"] == "player" and t.data["playerExists"]:
                    t.dump.remove(t.data["playerPos"])
                    _X,_Y = t.data["playerPos"]
                    t.griddata[_X][_Y]["data"] = "empty"
                    t.griddata[_X][_Y]["id"] = -1
                    t.g.delete(t.grid[_X][_Y])
                    t.grid[_X][_Y] = None
                t.griddata[X][Y]["data"] = t.data["chosenBall"]
                t.griddata[X][Y]["id"] = 1
                t.griddata[X][Y]["speed"] = int(t.object["speedinputwidget"].get())
                
                if t.data["chosenBall"] == "player":
                    t.grid[X][Y] = t.g.create_oval(X*10+3,Y*10+3,X*10+11,Y*10+11, fill="yellow", outline="yellow", tags=R[0])
                    t.data["playerExists"] = True; t.data["playerPos"] = (X,Y); BALL = "Player"
                elif t.data["chosenBall"] == "blue": t.grid[X][Y] = t.g.create_oval(X*10+3,Y*10+3,X*10+11,Y*10+11, fill="blue", outline="white", tags=R[0]); BALL = "Blue"
                elif t.data["chosenBall"] == "black": t.grid[X][Y] = t.g.create_oval(X*10+3,Y*10+3,X*10+11,Y*10+11, fill="black", outline="red", tags=R[0]); BALL = "Black"
                elif t.data["chosenBall"] == "mblue": t.grid[X][Y] = t.g.create_oval(X*10+3,Y*10+3,X*10+11,Y*10+11, fill="#222222", outline="#7777FF", width=2, tags=R[0]); BALL = "Blue Ring (speed "+t.object["speedinputwidget"].get()+")"
                elif t.data["chosenBall"] == "mred": t.grid[X][Y] = t.g.create_oval(X*10+3,Y*10+3,X*10+11,Y*10+11, fill="#222222", outline="#FF2222", width=2, tags=R[0]); BALL = "Red Ring (speed "+t.object["speedinputwidget"].get()+")"
                
                t.dump.add((X,Y))
                t.msg(f"Put {BALL} at {X+1}, {Y+1}")
           

        if len(R) == 2 and "ballchoice" in R[0]:
            ball = R[0].split("_")[1]
            t.data["chosenBall"] = ball
            if ball == "player": t.g.moveto(t.object["ballChooser"], 56, 413)
            if ball == "blue": t.g.moveto(t.object["ballChooser"], 76, 413)
            if ball == "black": t.g.moveto(t.object["ballChooser"], 96, 413)
            if ball == "mblue": t.g.moveto(t.object["ballChooser"], 116, 413)
            if ball == "mred": t.g.moveto(t.object["ballChooser"], 136, 413)
       
    def clickRight(t,e):
        R = t.g.gettags("current")
        if len(R) == 2 and R[0] != "current" and "ballchoice" not in R[0]:
            X,Y = map(int, R[0].split(";"))
            if (X,Y) in t.dump:
                t.dump.remove((X,Y))
                if t.griddata[X][Y]["data"] == "player":
                    t.data["playerExists"] = False; t.data["playerPos"] = (-1,-1)
                t.griddata[X][Y]["data"] = "empty"
                t.griddata[X][Y]["id"] = -1
                t.griddata[X][Y]["speed"] = 0
                t.g.delete(t.grid[X][Y])
                t.grid[X][Y] = None
                
                t.msg(f"Removed ball at {X+1}, {Y+1}")
                
    def validateSpeed(t):
        R = t.object["speedinputwidget"].get()
        try:
            R = int(R)
        except:
            t.msg("Invalid Speed Value.")
            return False
        else:
            if R < 1: 
                t.msg("Speed Value is too low.")
                return False
            elif R > 100:
                t.msg("Speed Value is too high.")
                return False
            else: return True
            
    def showHelp(t,e):
          messagebox.showinfo("Help", _info.EDITORHELP)

    def msg(t, txt):
          t.g.itemconfig(t.object["message"], text=txt)
          
    def die(t):
        t.w.destroy()
    def restoreOnDeath(t):
        t.rootWindow.deiconify()
        t.w.destroy()