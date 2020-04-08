from PMS_Loci_2 import *
from PMS_Map_4 import *
from tkinter import *
from tkinter import filedialog, Text, messagebox
import sqlite3
import os
import datetime
import pandas as pd


t=54
rl=11 #rows length
cl=10 #column length

def main():
    #Database Global Variable Declaration
    global root
    root=Tk() #build GUI
    root.title("FuSion Parking Manager")
    #global posi
    global mobi
    global vehicle
    #posi= IntVar()
    mobi= IntVar()
    vehicle=StringVar()

    canvas=Canvas(root, height=600, width=700, bg="#19191c")
    canvas.pack()

    frame= Frame(root, bg="#a3acff")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading=Label(root, text="FuSion Parking Management System",width=30,fg="black", bg ="yellow",font=("bold",22))
    heading.place(x=95,y=18)

    total1=Label(root, text="TOTAL",padx=62,pady=20,fg="white",font=(20), bg ="#000d40")
    total1.place(x=150,y=100) #Total Number of Slots

    total2=Label(root, text=t,padx=60,pady=20,fg="white",font=(20), bg ="#19191c")
    total2.place(x=330,y=100)

    avl1=Label(root, text="AVAILABLE",padx=41,pady=20,fg="white",font=(20), bg ="#0009bd")
    avl1.place(x=150,y=170) #Available Slots
    #av=addDB()
    avl2=Label(root, text=t-addDB(),padx=60,pady=20,fg="white",font=(20), bg ="#263D42")
    avl2.place(x=330,y=170)

    info1=Label(root, text="Enter the Vehicle Number",width=20,fg="white", bg="#696c70", font=("bold",19))
    info1.place(x=120,y=250) #Display text

    info2=Label(root, text="Enter the Contact Number",width=20,fg="white", bg="#696c70", font=("bold",19))
    info2.place(x=120,y=300) #Display text

    entry1=Entry(root,textvar=vehicle)
    entry1.place(x=450,y=250,height=40) #Enter Name

    entry2=Entry(root,textvar=mobi)
    entry2.place(x=450,y=300,height=40) #Enter contact

    #Park Button
    add=Button(root, text="PARK IN",padx=5,pady=20,fg="black",font=(15), bg ="green",command=database)
    add.place(x=150,y=350)
    #Find location Button
    find=Button(root, text="FIND VEHICLE",padx=1,pady=20,fg="black", bg ="yellow", font=(15),command=findLoc)
    find.place(x=250,y=350)
    #Remove Vehicle Button
    find=Button(root, text="PARK OUT",padx=1,pady=20,fg="black", bg ="red", font=(15),command=deleteDB)
    find.place(x=400,y=350)
    #close
    close=Button(root,text="FINISH",padx=15,pady=7,fg="black", bg ="grey", font=(17),command=action)
    close.place(x=250,y=547)

    root.resizable(0, 0) #lock maximize option
    root.mainloop()


#create connection to database
def startDB():
    try:
        conn = sqlite3.connect('Location5.db')
    except Error as e:
        print(e)

    return conn
#update location on map for filling
def loci():
    try:
        s,a,b=position()
    #print(temp[1][4])
        global rl
        df = pd.read_csv("map4.csv",usecols=range(1,rl))
        temp = df.to_numpy().tolist()
        temp[a][b]='T'
        pd.DataFrame(temp).to_csv("map4.csv")
        for i in temp:
            print(i)
        print("*******EOL******")


    except:
        print("OOPS!!! No more space available")




#create database

conn=startDB()
cursor=conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Location (Vehicle TEXT NOT NULL UNIQUE, Contact INT NOT NULL UNIQUE, Location_X INT, Location_Y INT,Date TEXT NOT NULL, Time TEXT NOT NULL)')
conn.commit()
cursor.close()

#add elements in database
def database():
    try:
        s,a,b=position()
    except Exception as e:
        s=0
        a=0
        b=0
        msg=messagebox.showinfo("Error!!!", "No more empty slots")
    now = datetime.datetime.now()
    Time=now.strftime("%H:%M:%S")
    Date=now.strftime("%d-%m-%Y")
    name=vehicle.get()
    try:
        mob=mobi.get()

    except Exception as e:
        msg=messagebox.showinfo("Error!!!", "Please Enter a valid Number")
        mob=0

    posx=a  #x-axis of Location
    posy=b  #y-axis of location
    try:
        conn=startDB()
        cursor=conn.cursor()
        #cursor.execute('CREATE TABLE IF NOT EXISTS Location (Vehicle TEXT NOT NULL, Contact INT NOT NULL, Location INT NOT NULL, Date TEXT NOT NULL, Time TEXT NOT NULL)')
        cursor.execute('INSERT INTO Location (Vehicle, Contact, Location_X, Location_Y, Date, Time) VALUES(?,?,?,?,?,?)',(name,mob,posx,posy,Date,Time))
        conn.commit()
        cursor.close()
        msg=messagebox.showinfo("Park Vehicle","Park your Vehicle at (%d,%d)"%(posx,posy))
        park()
    except Exception as error:
        msg=messagebox.showinfo("Duplicate Error", "Please Enter Unique Elements")
    finally:
        if (conn):
            conn.close()


#counts total vehicle in database
def addDB():
    conn = startDB()
    cursor=conn.cursor()
    cursor.execute("SELECT count(*) FROM Location")
    result=cursor.fetchone()[0]
    return result
    cursor.close()
#park button
def park():
    #database()
    loci()
    aval()
    disp() #display parking slots on GUI

#Delete vehicle from database
def deleteDB():

    try:

        conn = startDB()
        cursor = conn.cursor()
        name=vehicle.get()
        try:
            mob=mobi.get()
        except:
            msg=messagebox.showinfo("Error!!!", "Please Enter a valid Number")
            mob=0
        try:
            sql_select_query = """SELECT * from Location where Vehicle= ? AND Contact=?"""
            cursor.execute(sql_select_query, (name,mob))
            row=cursor.fetchall()
            while row:
                a1=row[0][2]
                b1=row[0][3]
                break
            #update location on map for filling
            global rl
            df = pd.read_csv("map4.csv",usecols=range(1,rl))
            temp = df.to_numpy().tolist()
            temp[a1][b1]='E'
            pd.DataFrame(temp).to_csv("map4.csv")
            for i in temp:
                print(i)
            print("*******EOL******")

            sql_delete_query = """DELETE from Location where Vehicle= ? AND Contact=?"""
            cursor.execute(sql_delete_query, (name,mob))

            conn.commit()
            cursor.close()
            aval() #update available slots
            disp() #display available slots
        except sqlite3.Error as error:
            msg=messagebox.showinfo("Delete Failed", "Vehicle does not Exist")


    except Exception as error:
        msg=messagebox.showinfo("Delete Failed", "Vehicle not found")
    finally:
        if (conn):
            conn.close()
#give location from database
def findLoc():
    try:
        conn = startDB()
        cursor = conn.cursor()
        name=vehicle.get()
        mob=mobi.get()
        sql_select_query = """SELECT * from Location where Vehicle= ? AND Contact=?"""
        cursor.execute(sql_select_query, (name,mob))
        row=cursor.fetchall()
        flag=1
        while row:
            flag=0
            msg=messagebox.showinfo("Vehicle Found","Vehicle parked at (%d,%d)"%(row[0][2],row[0][3]))
            disp()
            break
        if(flag==1):
            msg=messagebox.showinfo("Error!!!", "No Matching Vehicle Found")
        conn.commit()
        cursor.close()

    except Exception as error:
        msg=messagebox.showinfo("Error!!!", error)

    finally:
        if (conn):
            conn.close()



#update available slots
def aval():
    global t
    o=0
    p=addDB()
    o=t-p

    avl2=Label(root, text=o,padx=60,pady=20,fg="white",font=(20), bg ="#263D42")
    avl2.place(x=330,y=170)
#close application
def action():
    msg=messagebox.showinfo("Finished!!!","Thank You for using FuSion Parking Management Software ")
    root.destroy()
    #shut()




#if __name__ == '__main__':

    #main_account_screen()
