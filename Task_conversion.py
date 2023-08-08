from tkinter import *

def convert_to_gram():
    kg=int(n1.get())
    grams = kg*1000
    print(grams)
    
def convert_to_kilogram():
    g=int(m1.get())
    kilograms = g/1000
    print(kilograms)
    


win= Tk()

d1= Label(win,text="weight converter",font=('Arial',20),foreground="green")
d1.pack()

c1=Label(win,text="Enter the weight")
c1.pack()

n1 = Entry(win,textvariable= "kg")
n1.pack()

m1 = Entry(win,textvariable="g")
m1.pack()


convertbtn = Button(win,text="convert to gram",command=convert_to_gram)
convertbtn.pack()

convertkgbtn = Button(win,text="convert to kilogram",command=convert_to_kilogram)
convertkgbtn.pack()

win.mainloop()