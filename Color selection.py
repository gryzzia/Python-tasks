# Условие: при нажатии на кнопку выбора цвета, фон заливается выбранным цветом
# Condition: when you click on the color selection button, the background is filled with the selected color
li=['red',]
li1=['green']
li2=['blue']
def color(event):
    root.configure(bg=li[0])
def color1(event):
    root.configure(bg=li1[0])
def color2(event):
    root.configure(bg=li2[0])
    

from tkinter import *
root=Tk()



but=Button(root,text='red')
but1=Button(root,text='green')
but2=Button(root,text='blue')


but.pack()
but1.pack()
but2.pack()

but.bind("<Button-1>",color)
but1.bind("<Button-1>",color1)
but2.bind("<Button-1>",color2)

root.mainloop()
