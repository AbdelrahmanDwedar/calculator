from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('350x300')
window.resizable(width=False, height=False)

y = " "
x = StringVar()
def fnSet(num):
    global y 
    y = y + str(num)
    x.set(y)
def result():
    res = str(eval(y))
    x.set(res)
def clear():
    global y
    y = " "
    x.set(y)

screen = Entry(window,width=25,font=('Time',16,'bold'),bg='powder blue',textvariable = x)
screen.place(x=25,y=30)

btn7 = Button(text='7',width=8,command = lambda:fnSet(7))
btn7.place(x=25,y=75)

btn8 = Button(text='8',width=8,command = lambda:fnSet(8))
btn8.place(x=100,y=75)

btn9 = Button(text='9',width=8,command = lambda:fnSet(9))
btn9.place(x=175,y=75)

btn4 = Button(text='4',width=8,command = lambda:fnSet(4))
btn4.place(x=25,y=120)

btn5 = Button(text='5',width=8,command = lambda:fnSet(5))
btn5.place(x=100,y=120)

btn6 = Button(text='6',width=8,command = lambda:fnSet(6))
btn6.place(x=175,y=120)

btn3 = Button(text='3',width=8,command = lambda:fnSet(3))
btn3.place(x=25,y=165)

btn2 = Button(text='2',width=8,command = lambda:fnSet(2))
btn2.place(x=100,y=165)

btn1 = Button(text='1',width=8,command = lambda:fnSet(1))
btn1.place(x=175,y=165)

btnp = Button(text='+',width=8,bg="yellow",command = lambda:fnSet('+'))
btnp.place(x=250,y=75)

btnm = Button(text='-',width=8,bg="yellow",command = lambda:fnSet('-'))
btnm.place(x=250,y=105)

btnmt = Button(text='X',width=8,bg="yellow",command = lambda:fnSet('*'))
btnmt.place(x=250,y=135)

btnd = Button(text='%',width=8,bg="yellow",command = lambda:fnSet('/'))
btnd.place(x=250,y=165)


btnequal = Button(text="=",width=12,bg='white',command=result)
btnequal.place(x=25,y=200)


btnclear = Button(text="C",width=12,bg='white',command=clear)
btnclear.place(x=125,y=200)

btn0 = Button(text='0',width=12,command = lambda:fnSet(0))
btn0.place(x=225,y=200)

window.mainloop()