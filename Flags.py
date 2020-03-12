# Условие задачи: Пользователь отмечает 1 из трех флажков, при нажатии на кнопку программа должна показать какой флажок он выбрал
# Condition of the task: The user marks 1 of the three flags, when you click on the button, the program should show which flag he selected
def display(event):
    v=var.get()
    if v==0:
      lbl['text']='vkl 1-ya knopka'
    elif v==1:
        lbl['text']='vkl 2-ya knopka'
    elif v==2:
         lbl['text']='vkl 3-ya knopka'
from tkinter import*
root=Tk()
var=IntVar()
var.set(1)

rad0=Radiobutton(root,text='first', variable=var,value='0')
rad1=Radiobutton(root,text='second', variable=var,value='1')
rad2=Radiobutton(root,text='znak', variable=var,value='2')
but=Button(root,text='znachenie')
but.bind('<Button-1>',display)
but.place(x=20,y=50)
rad0.pack()
rad1.pack()
rad2.pack()
lbl=Label(root, width=80)
lbl.pack()
root.mainloop()
