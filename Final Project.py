from tkinter import *
from tkinter import simpledialog
import sqlite3

window = Tk()
window.title("Contacts")

connection = sqlite3.connect("Contacts_db.db")
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Person (
    Name text,
    Number integer
    )""")
connection.commit()

#Messages Variables
text_m = StringVar()
text_v = StringVar()

#Loading icon and picture
pic = PhotoImage(file="phone.png")
window.iconphoto(False,pic)
window.geometry('900x700')

def raise_frame(frame, aux):
    if aux == 1:
        searchWindow.grid_forget()
        mainWindow.grid(row=2, column=0,columnspan=2)
    else:
        mainWindow.grid_forget()
        searchWindow.grid(row=2, column=0,columnspan=2)
    #frame.tkraise()
        
def Keyboard_Input(n):
    current_number = Number_entry.get()
    Number_entry.delete(0, END)
    Number_entry.insert(0, str(current_number) + str(n))

def db_saver():
    nom=Name_Entry_1.get()
    num=Number_entry.get()
    if nom!="" and num!="":
        if num.isdigit():
            c.execute("SELECT * FROM Person ")
            list_P = c.fetchall() #we get back a list of tuples
            t1 = True
            for l in list_P:
                if l[0]== nom:
                    t1 = False
                    break
            if t1:
                c.execute("INSERT INTO Person VALUES (?, ?)",(nom, num))
                connection.commit()
                Lista.insert(END, nom)
                text_m.set("Saved Succesfully!")
            else:
                text_m.set("Name Is Already Saved!")
            
    else:
        text_m.set("One or more fields are empty.")

def db_searcher():
    x=Name_Entry_2.get()
    if x=="":
        text_v.set("Empty Field.")
    else:
        #f=open("repertoire.txt","r")
        c.execute("SELECT * FROM Person WHERE Name=?", (x,))
        ray = c.fetchone()
        if type(ray) == tuple  :
            text_v.set(ray[1])
        else:
            text_v.set("There is no number with that name")
def List_show():
    c.execute("SELECT * FROM Person")
    ray = c.fetchall()
    for i in ray:
        Lista.insert(END, i[0])

def Delete_P():
    D = Lista.get(ANCHOR)
    if D != "":
        c.execute("DELETE FROM Person WHERE Name=?", (D,))
        connection.commit()
        Lista.delete(ANCHOR)

def Update_P():
    D = Lista.get(ANCHOR)
    if D != "":
        s = simpledialog.askinteger("Contact Update", "Please Enter The New Number For " + D)
        if s is not None:
            c.execute("UPDATE Person SET Number = ? WHERE Name=?", (s,D))
            connection.commit()
                
#Main Frame
Container = Frame(window)

#First Buttons
Button(Container, text = "Save Contacts", font = "Verdana 15 bold",width=30, height=2,bg="#9F9F9F", command=lambda:raise_frame(mainWindow,1)).grid(row=0, column=0)
Button(Container, text = "Search For Contacts",font = "Verdana 15 bold",width=30, height=2,bg="#9F9F9F", command=lambda:raise_frame(searchWindow,2)).grid(row=0, column = 1)

#Contacts Picture
canvas=Canvas(Container,width=300,height=70)
canvas.grid(row=1,column=0,columnspan=2)
canvas.create_image(130, 5, anchor=NW, image=pic)

#mainWindow
mainWindow = LabelFrame(Container)
 
Label(mainWindow, text = "Name :", font = "Verdana 16", anchor="w").grid(row=0,column=0)

Name_Entry_1=Entry(mainWindow,width=30, borderwidth=3)
Name_Entry_1.grid(row=0,column=1)

Label(mainWindow, text = "Number :", font = "Verdana 16 ", anchor="w").grid(row=1,column=0)

Number_entry=Entry(mainWindow,width=30, borderwidth=3)
Number_entry.grid(row=1,column=1)

Valid=Button(mainWindow, text = "Add",width=20, height=1,bg="#9F9F9F", command = db_saver)
Valid.grid(row=2,column=1)

res = Label(mainWindow, textvariable =text_m, fg="red")
text_m.set("")
res.grid(row=3,column=1)

#searchWindow
searchWindow = Frame(Container)

Label(searchWindow, text = "Name :", font = "Helvetica 20").grid(row=0,column=0,sticky=E)

Name_Entry_2=Entry(searchWindow,width=30, borderwidth=3)
Name_Entry_2.grid(row=0,column=1, sticky=W)

Valid_1=Button(searchWindow, text = "Submit",width=25,bg="#9F9F9F", command = db_searcher)
Valid_1.grid(row=1,column=1,sticky=W)

res = Label(searchWindow,fg="red", textvariable =text_v,)
text_v.set("")
res.grid(row=2,column=1)


L = LabelFrame(searchWindow, text = "List :", font = "Helvetica 15")
L.grid(columnspan = 2)


#listBox
Lista = Listbox(L,height = 15, font = "Times 13")
Lista.grid(row=0,column=0,rowspan=2)
List_show()

B_Update=Button(L, text = "Update", width=8,bg="#9F9F9F", command = Update_P)
B_Update.grid(row=0,column=1,sticky=S)

B_Delete=Button(L, text = "Delete", width=8,bg="#9F9F9F", command = Delete_P)
B_Delete.grid(row=1,column=1, sticky=N)

#mainWindow appears first
mainWindow.grid(row=2, column=0,columnspan=2)

#Keyboard
Clavier=LabelFrame(mainWindow, bg="#ffffff")
Clavier.grid(row=4,column=0, columnspan=2)

buttonxx,buttonyy=4,10

B_0=Button(Clavier, text=0, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(0))
B_1=Button(Clavier, text=1, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(1))
B_2=Button(Clavier, text=2, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(2))
B_3=Button(Clavier, text=3, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(3))
B_4=Button(Clavier, text=4, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(4))
B_5=Button(Clavier, text=5, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(5))
B_6=Button(Clavier, text=6, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(6))
B_7=Button(Clavier, text=7, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(7))
B_8=Button(Clavier, text=8, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(8))
B_9=Button(Clavier, text=9, padx=buttonxx,pady=buttonyy,font='Helvetica 25 bold', command=lambda: Keyboard_Input(9))
        
B_0.grid(row=1,column=0)
B_1.grid(row=1,column=1)
B_2.grid(row=1,column=2)
B_3.grid(row=1,column=3)
B_4.grid(row=1,column=4)

B_5.grid(row=2,column=0)
B_6.grid(row=2,column=1)
B_7.grid(row=2,column=2)
B_8.grid(row=2,column=3)
B_9.grid(row=2,column=4)



#Main
Container.pack()

window.mainloop()
connection.close()
