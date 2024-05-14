import tkinter

class Editor:
    def __init__(t):
        t.w = tkinter.Toplevel()
        t.w.title("KOULA LEVEL EDITOR")
        t.w.iconbitmap("gamedata/other/_favicon.ico")
        t.w.config(cursor="none")
        t.g = tkinter.Canvas(t.w, bg="#222222",width=400,height=535,cursor="plus")
        t.g.pack()

        t.object = {}
        t.object["line"] = t.g.create_line(0, 405, 405, 405, fill="white")

        t.griddata = []
        for i in range(40):
            row = []
            for j in range(40):
                row.append({"data": "empty", "id": -1})
            t.griddata.append(row)

        t.grid = []
        for i in range(40):
            row = []
            for j in range(40):
                row.append(t.g.create_rectangle(j*10,i*10,j*10+10,i*10+10, tags=str(j)+";"+str(i), width=0))

        t.g.bind_all('<ButtonPress-1>', t.click)
    def click(t,e): print(t.g.gettags("current"))
