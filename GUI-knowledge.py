from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()  #T must be upper,
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #size widthxheight

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('AngsanaNew',30),fg='green')
L1.place(x=58,y=20)



#######################################
def Button2():
    text = 'We have 300 baht'
    messagebox.showinfo('Account Balance',text)



FB1 = LabelFrame(GUI,text='Money') #board
FB1.place(x=100,y=80) #define frame
B2 = ttk.Button(FB1,text='How much we have?',command=Button2) # put buttom  in FB1 and link command Button2s
B2.pack(ipadx=20,ipady=20,padx=30,pady=2) # pad is label frame , ipad is place of button2 
########################################

def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('I studied',text)



FB2 = LabelFrame(GUI,text='Study Schedule') #board
FB2.place(x=100,y=200) #define frame
B3 = ttk.Button(FB2,text='What I Studied this week?',command=Button3) # put buttom  in FB1 and link command Button2s
B3.pack(ipadx=20,ipady=20,padx=30,pady=2) # pad is label frame , ipad is place of button2 
########################################








GUI.mainloop()
