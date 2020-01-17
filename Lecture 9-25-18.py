#9-25-18 Lecture

from tkinter import *

#creating Stacks -------------

class Stack:
    
    #constructor
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return len(self.items)==0

#creating the parentheses check method ---------------

def parenthesesCheck():
    someString = p.get()
    parentheses = Stack()
    balanced = True
    index = 0

    while index < len(someString) and balanced:
        if someString[index] == '(':
            parentheses.push(someString[index])
        else:
            if parentheses.isEmpty():
                balanced = False
            else:
                parentheses.pop()
        index = index + 1

    if balanced and parentheses.isEmpty():
        result.set('Balanced')
    else:
        result.set('UnBalanced')

def clearEntry():
    p.delete(0,END)

#create main window ----------------

win = Tk()
win.title('Parenthesis Checker')
win.geometry('300x100')

p = Entry(win, width = 20)
p.grid(column = 150, row = 10)
result = StringVar()

btn = Button(win, text = 'Check', command = parenthesesCheck)
btn.grid(column = 150, row = 40)

clearBtn = Button(win, text = 'Clear', command = clearEntry)
clearBtn.grid(column = 150, row = 60)

resultLbl = Label(win, textvariable = result)
resultLbl.grid(column = 150, row = 200)


win.mainloop()
