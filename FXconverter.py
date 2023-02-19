from tkinter import *
from tkinter import ttk
from tkinter import messagebox



GUI = Tk()
GUI.title('Foreign Currency Converter')
GUI.geometry('400x400')

L1 = Label(GUI,text='FX to Thai Baht',font=('Imprint MT Shadow',30),fg='green')
L1.place(x=60,y=150)

USDFX = int(33.63)
GBPFX = int(40.57)
JPYFX = int(0.26)
KRWFX = int(0.027)

def Button1():
    text = 'USD ' +  str(int(E1.get())) + ' is THB ' + str(int(E1.get())*33.63)
    messagebox.showinfo('Result',text)

L2 = Label(GUI,text ='USD:',font=('Arial',12),fg='black')
L2.grid(row=4,column=2,padx=1,pady=0,sticky='W')

E1 = Entry(GUI)
E1.grid(row=4,column=3,padx=1,pady=0)

B1 = ttk.Button(GUI,text='Convert',command=Button1)
B1.grid(row=4,column=4,padx=1,pady=0,columnspan=2)

def Button2():
    text = 'GBP ' +  str(int(E2.get())) + ' is THB ' + str(int(E2.get())*40.57)
    messagebox.showinfo('Result',text)

L3 = Label(GUI,text ='GBP:',font=('Arial',12),fg='black')
L3.grid(row=5,column=2,padx=1,pady=0,sticky='W')

E2 = Entry(GUI)
E2.grid(row=5,column=3,padx=1,pady=0)

B2 = ttk.Button(GUI,text='Convert',command=Button2)
B2.grid(row=5,column=4,padx=1,pady=0,columnspan=2)


def Button3():
    text = 'JPY ' +  str(int(E3.get())) + ' is THB ' + str(int(E3.get())*0.26)
    messagebox.showinfo('Result',text)

L4 = Label(GUI,text ='JYP:',font=('Arial',12),fg='black')
L4.grid(row=6,column=2,padx=1,pady=0,sticky='W')

E3 = Entry(GUI)
E3.grid(row=6,column=3,padx=1,pady=0)

B3 = ttk.Button(GUI,text='Convert',command=Button3)
B3.grid(row=6,column=4,padx=1,pady=0,columnspan=2)


def Button4():
    text = 'KRW ' +  str(int(E4.get())) + ' is THB ' + str(int(E4.get())*0.027)
    messagebox.showinfo('Result',text)

L5 = Label(GUI,text ='KRW:',font=('Arial',12),fg='black')
L5.grid(row=7,column=2,padx=1,pady=0,sticky='W')

E4 = Entry(GUI)
E4.grid(row=7,column=3,padx=1,pady=0)

B4 = ttk.Button(GUI,text='Convert',command=Button4)
B4.grid(row=7,column=4,padx=1,pady=0,columnspan=2)


GUI.mainloop()
