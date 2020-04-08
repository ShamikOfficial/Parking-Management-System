import pandas as pd
from tkinter import *


#command line print
'''for i in temp:
    for j in i:
        if(j=="P"):
            print(" 0 ",end="\t")
        if(j=="E"):
            print("[ ]",end="\t")
        if(j=="S"):
            print(" -> ",end="\t")
        if(j=="T"):
            print(" X ",end="\t")
    print("\n")
'''


def disp():
    global rl
    global cl
    rl=11 #rows length
    cl=10 #column length
    df = pd.read_csv("map4.csv",usecols=range(1,rl))
    temp = df.to_numpy().tolist()
    pd.DataFrame(temp).to_csv("map4.csv")
    root1 = Tk() #build GUI
    root1.title("Live Parking Slots")
    root1.geometry("500x700")
    frame=Frame(root1)
    Grid.rowconfigure(root1, 0, weight=1)
    Grid.columnconfigure(root1, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    grid=Frame(frame)
    grid.grid(sticky=N+S+E+W, column=0, row=rl+1, columnspan=2)
    Grid.rowconfigure(frame, rl, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    #building hit map
    for x in range(rl):
        for y in range(10):
            if(temp[x][y]=="P"):
                btn = Button(frame, bg="grey")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
            if(temp[x][y]=="E"):
                btn = Button(frame, bg="yellow")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
            if(temp[x][y]=="S"):
                btn = Button(frame, bg="blue",)
                btn.grid(column=x, row=y, sticky=N+S+E+W)
            if(temp[x][y]=="T"):
                btn = Button(frame,bg="red")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
    #btn = Button(frame)
    #btn.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(rl):
      Grid.columnconfigure(frame, x, weight=6)

    for y in range(10):
      Grid.rowconfigure(frame, y, weight=5)

    root1.mainloop()
#print("*******EOL******")
def shut():
    root1.destroy()
#run below function to check this module only
#disp()
