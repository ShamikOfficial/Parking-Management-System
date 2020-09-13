import pandas as pd
from tkinter import *
import os

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
    
    #rl=10 #rows length
    #cl=11 #column length
    df = pd.read_csv('Data'+os.path.sep+"map4.csv",header=None)
    rl = df.shape[1]  # gives number of row count
    cl = df.shape[0]  # gives number of col count
    df.dropna(axis=0)
    #print(rl,cl,df)
    #df = pd.read_csv("map4.csv",usecols=range(1,rl))
    temp = df.values.tolist()
    #print(temp)
    #pd.DataFrame(temp).to_csv("map4.csv",header=None,index=False)
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
    emp_count=0
    filled_count=0
    for x in range(cl):
        #print(x)
        for y in range(rl):
            #print(y)
            if(temp[x][y]=="P"):
                btn = Button(frame, bg="grey")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
            if(temp[x][y]=="E"):
                btn = Button(frame, bg="yellow")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
                emp_count+=1
            if(temp[x][y]=="S"):
                btn = Button(frame, bg="blue",)
                btn.grid(column=x, row=y, sticky=N+S+E+W)
            if(temp[x][y]=="T"):
                btn = Button(frame,bg="red")
                btn.grid(column=x, row=y, sticky=N+S+E+W)
                filled_count+=1
    #btn = Button(frame)
    #btn.grid(column=x, row=y, sticky=N+S+E+W)
    for x in range(cl):
      Grid.columnconfigure(frame, x, weight=6)

    for y in range(rl):
      Grid.rowconfigure(frame, y, weight=5)

    root1.mainloop()
#print("*******EOL******")
def shut():
    root1.destroy()
#run below function to check this module only
#disp()
