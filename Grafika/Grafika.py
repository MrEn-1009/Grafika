from tkinter import *
klik=0
def plaz(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def pluz(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def pliz(event):
    tht=txt.get()
    lbl.configure(text=tht)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik) 
def vih(event):
    okno.destroy()
okno=Tk()
okno.title('dskjgdn')
okno.geometry('1000x450')
knopka=Button(okno,text='Не трогать!',font='Arial 16',fg='black',bg='red',height=4,width=14,relief=GROOVE)
knopka.bind('<Button-1>',plaz)
knopka.bind('<Button-3>',pluz)
knop=Button(okno,text='Выход',font='Arial 16',fg='black',bg='red',height=4,width=14,relief=GROOVE)
knop.bind('<Button-1>', vih)
lbl=Label(okno,text='',height=4,width=14,font='Arial 16',fg='red',bg='black')
txt=Entry(okno,width=14,font='Arial 16',fg='black',bg='white',justify=CENTER)
txt.bind('<Return>',pliz)
i1=PhotoImage(file='1.gif')
var=StringVar()
var.set('Один')
r1=Radiobutton(okno,image=i1,variable=var,value='Один',command=valik)
lbl.pack()
knopka.pack()
txt.pack()
knop.pack()
okno.mainloop()