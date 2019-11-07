#imports
from tkinter import *
import random
from tkinter import messagebox
import time
import datetime
from PyMySQL import pymysql as p
from guiwidgets.listview import MultiListbox

#declarations
root=Tk()
root.geometry("1600x8000")
root.title("Online Book Selling System")
Tops=Frame(root, width=1600)
Tops.pack(side=TOP)
f1=Frame(root,width=1000,height=600,padx=40,pady=40)
f1.pack(side=LEFT,fill=Y,expand=True)
localtime=datetime.datetime.now()
localtime=localtime.strftime("%A, %d %B %Y \t %I:%M %p")

l1=[]
#===============================Database==============================================================================
db =p.connect("localhost","root","","bill" )
cursor = db.cursor()
sql="SELECT * from menu"
try:
   # Execute the SQL command
    cursor.execute(sql)
   # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        item=row[1]
        l1.append(item)
except:
    print ("Error: unable to fetch data")
#======================================================================================================================
tkvar = StringVar(root)
tkvar.set("--NO DISH SELECTED--")
qtvar = StringVar(root)
qtvar.set(0)
f2=Frame(root,width=800,height=700,borderwidth=2,relief="solid",padx=40,pady=40)
f2.pack(side=RIGHT,expand=True)
global total
total=0
tot=StringVar()
cgst=StringVar()
sgst=StringVar()
gtot=StringVar()
tot.set("Total = ₹")
cgst.set("CGST = ₹")
sgst.set("SGST = ₹")
gtot.set("Grand Total = ₹")

#command methods
def selen(*args):
    if(tkvar.get()!=" "):
        btnAdd.config(state='active')

def qExit():
    root.destroy()
def mAdd():
    global total
    x=tkvar.get()
    try:
        y=int(qtvar.get())
    except:
        messagebox.showinfo("Error!", "Please Enter Valid Quantity")

    price=query(x)
#error line
    amt=int(qtvar.get())*price
    li=[x,y,price,amt]
    mlb.insert(0,li)
    qtvar.set(0)
    total=total+amt    

    
def query(y):
    checksql="SELECT cost from menu WHERE item='%s'" %(y)
    cursor.execute(checksql)
    results = cursor.fetchone()
    return results[0]  
    
def calctotal():
    global total
    gst=0.05*total
    grandtot=total+(2*gst)
    tot.set("Total = ₹"+str(total))
    cgst.set("CGST = ₹"+str(gst))
    sgst.set("SGST = ₹"+str(gst))
    gtot.set("Grand Total = ₹"+str(grandtot))

def Reset():
    mlb.delete(0,END) #multi list box is used to display data in tables
    tot.set("Total = ₹")
    cgst.set("CGST = ₹")
    sgst.set("SGST = ₹")
    gtot.set("Grand Total = ₹")
    tkvar.set("--NO DISH SELECTED--") #drop down
    lblReference= Label(Tops,font=('arial',20, 'bold'),text="Bill Number:"+str(random.randint(10908,500876)),fg="brown",bd=10,borderwidth=4,relief="solid",padx=10,pady=10).grid(row=1,column=1)
    qtvar.set(0)

#GUI
#headings(top)
lblInfo=Label(Tops,font=('arial black',50,'bold','underline'),text="\tLe Livre",fg="purple",padx=10,pady=10).grid(row=0,column=0)
lblTime=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="dark blue",padx=10,pady=10).grid(row=1,column=0)
lblReference= Label(Tops,font=('arial',20, 'bold'),text="Bill Number:"+str(random.randint(10908,500876)),fg="brown",bd=10,borderwidth=4,relief="solid",padx=10,pady=10).grid(row=1,column=1)
lblType= Label(Tops,font=('arial',20,'bold'),text="Dine In",fg="Steel Blue",padx=10,pady=10).grid(row=1,column=2)

#left side(f1)
lblCh=Label(f1, text="Choose a dish:",font=('arial',20,'bold'),borderwidth=2,relief="solid",padx=10,pady=10).grid(row = 5, column =0)
popupMenu = OptionMenu(f1, tkvar, *l1,command=selen)
popupMenu.config(width=30)
popupMenu.grid(row = 5, column =1)
lblQty=Label(f1, text="Enter Quantity:-",font=('calibri',20,'bold'),borderwidth=2,relief="solid",padx=18.5,pady=10).grid(row = 8, column =0)
txtQty=Entry(f1, font=('calibri',16,'bold'),textvariable=qtvar,relief='solid').grid(row=8,column=1)
btnTot=Button(f1,bd=20,fg="black",bg="light green",font=('arial',16,'bold'),width=10,text="Total",command=calctotal,padx=10,pady=10).grid(row=9,column=1)
btnExit=Button(f1,bd=20,fg="white",font=('arial',16,'bold'),width=10,text="Exit",bg="gray",command=qExit,padx=10,pady=10).grid(row=10,column=0)
btnAdd=Button(f1,bd=20,fg="black",font=('arial',16,'bold'),width=10,text="Add",bg="light blue",command=mAdd,padx=10,pady=10,state='disabled')
btnAdd.grid(row=9,column=0)                                                                                                                  
btnReset=Button(f1,bd=20,fg="white",font=('arial',16,'bold'),width=10,text="Reset",bg="gray",command=Reset,padx=10,pady=10).grid(row=10,column=1)
#btnPrint=Button(f1,bd=20,fg="black",bg="light green",font=('arial',16,'bold'),width=10,text="Print",command=printing,padx=10,pady=10).grid(row=2,column=1)

                                                                                                                 
#right side(f2)                                                                                                    
mlb=MultiListbox(f2,(('Name',20),('Quantity',20),('Price',20),('Amount',20)))
mlb.grid(row=5,column=1)
lblTotal=Label(f2, font=('arial', 16, 'bold'),bd=10,anchor="w",fg="dark green",textvariable=tot).grid(row=7, column=1)
lblCgst=Label(f2, font=('arial', 16, 'bold'),textvariable=cgst,bd=10,anchor="w",fg="dark green").grid(row=8, column=1)
lblSgst=Label(f2, font=('arial', 16, 'bold'),textvariable=sgst,bd=10,anchor="w",fg="dark green").grid(row=9, column=1)
lblGrandt=Label(f2, font=('arial', 16, 'bold'),textvariable=gtot,bd=10,anchor="w",fg="dark green").grid(row=10, column=1)


#end
root.mainloop()
