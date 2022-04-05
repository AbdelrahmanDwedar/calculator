from tkinter import *

window = Tk()
window.title('Calculator')
window.config(bg="#686868")
window.geometry('350x300')
window.resizable(width=False, height=False)

current_value = ""
screen_contects = StringVar()

screen = Entry(window,width=25,font=('Time',16,'bold'),bg='powder blue',textvariable = x)
screen.place(x=25,y=30)

def setNumber(num):
    global current_value
    current_value += str(num)
    screen_contects.set(current_value)

btn8 = Button(text='8',width=8,command = lambda:fnSet(8))
btn8.place(x=100,y=75)

def getResult():
    result = str(eval(current_value))
    # current_value = result
    screen_contects.set(result)

btn4 = Button(text='4',width=8,command = lambda:fnSet(4))
btn4.place(x=25,y=120)

def clear():
    global current_value
    current_value = ""
    screen_contects.set(current_value)

btn6 = Button(text='6',width=8,command = lambda:fnSet(6))
btn6.place(x=175,y=120)

screen = Entry(window, width = 19, font = ('Time', 16, 'bold'), textvariable = screen_contects, state='disabled')
screen.place(x = 25, y = 30)
screen.config(bg="#232323", border=0)

btn2 = Button(text='2',width=8,command = lambda:fnSet(2))
btn2.place(x=100,y=165)

btnNumber0 = Button(text = '0', width = 7, command = lambda:setNumber(0), border=0)
btnNumber0.place(x = 234, y = 200)

btnNumeber1 = Button(text = '1', width = 5, command = lambda:setNumber(1), border=0)
btnNumeber1.place(x = 175, y = 165) 

btnNumber2 = Button(text = '2', width = 5,command = lambda:setNumber(2), border=0)
btnNumber2.place(x = 100, y = 165)

btnNumber3 = Button(text = '3', width = 5, command = lambda:setNumber(3), border=0)
btnNumber3.place(x = 25, y = 165)

btnNumber4 = Button(text = '4', width = 5, command = lambda:setNumber(4), border=0)
btnNumber4.place(x = 25, y = 120)

btnNumber5 = Button(text = '5', width = 5, command = lambda:setNumber(5), border=0)
btnNumber5.place(x = 100, y = 120)

btnNumber6 = Button(text = '6', width = 5, command = lambda:setNumber(6), border=0)
btnNumber6.place(x = 175, y = 120)

btnNumber7 = Button(text = '7', width = 5, command = lambda:setNumber(7), border=0)
btnNumber7.place(x = 25, y = 75)

btnNumber8 = Button(text = '8', width = 5, command = lambda:setNumber(8), border=0)
btnNumber8.place(x = 100, y = 75)

btnNumber9 = Button(text = '9', width = 5, command = lambda:setNumber(9), border=0)
btnNumber9.place(x = 175, y = 75)

# ! setup the operations buttons 
btnPlus = Button(text = '+', width = 5, bg = "yellow", command = lambda:setNumber('+'), border=0)
btnPlus.place(x=250,y=75)

btnMinus = Button(text = '-', width = 5, bg = "yellow", command = lambda:setNumber('-'), border=0)
btnMinus.place(x=250,y=105)

btnMultiply = Button(text = '×', width = 5, bg = "yellow", command = lambda:setNumber('*'), border=0)
btnMultiply.place(x=250,y=135)

btnDivide = Button(text = '÷', width = 5, bg = "yellow", command = lambda:setNumber('/'), border=0)
btnDivide.place(x = 250, y = 165)

btnEqual = Button(text = "=", width = 7, bg = 'white', command = getResult, border=0)
btnEqual.place(x = 25, y = 200)

# ! clearing the screen
btnClear = Button(text = "Clear", width = 7, bg = 'white', command = clear, border=0)
btnClear.place(x = 125, y = 200)

window.mainloop()