#Условие данной задачи: создайте 2 текстовых поля и кнопку,при нажатии на которую происходит вычисление наибольшего значения введенного пользователем
from tkinter import *
root=Tk()

def c(event):
    a=ent.get()
    b=ent1.get()
    if a>b:
        print (a)
    elif a<b:
        print (b)
    elif a==b:
        print ('=')

root['width']=500
root['height']=300
ent=Entry(root, width='20',bd='3')
ent.pack()
ent1=Entry(root, width='20',bd='3')
ent1.pack()
but=Button(root,text='Вычислить')
but.place(x=20,y=50)
but.bind('<Button-1>',c)
but.pack()
root.mainloop()
