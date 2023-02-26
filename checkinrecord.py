from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

##############CSV##################
import csv

def writecsv(datalist):
    with open('data-checkin.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) # fw file writer
        fw.writerow(datalist) 

def readcsv():
    with open('data-checkin.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) # fr file reader 
        data = list(fr)
    return data

data = readcsv()

 
#####################################
GUI = Tk()  #T must be upper,
GUI.title('โปรแกรมบันทึกชื่อนักเรียนก่อนเข้าแถว') #ชื่อโปรแกรม
GUI.geometry('380x350') #size widthxheight



L1 = Label(GUI,text='โรงเรียนประถมเทตัน 帝丹小学校',font=('AngsanaNew',15),fg='Salmon')
L1.place(x=50,y=20)
###################################


LF1 = ttk.LabelFrame(GUI, text='กรอกชื่อนักเรียน')
LF1.place(x=58,y=80)

v_data = StringVar() #varia stores data in gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime


def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() # pull variable v_data 
    text = [t,data] #[time, data from fill the box]
    writecsv(text) #record on Csv
    v_data.set('') # clear the fulfill box

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)


GUI.mainloop()
