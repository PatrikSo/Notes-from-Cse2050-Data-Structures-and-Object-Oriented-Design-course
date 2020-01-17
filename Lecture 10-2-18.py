#10-2-18 Lecture

'''
(A + (B * C) + D)     infix
A B C * + D +         postfix
++ A * B C D          prefix
'''
#Basic stack class
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

#Postfix Algorithm
def postFix(expression):
    opstack = Stack()
    L = expression.split()
    Output = []
    
    operators = {'*':2, '/':2, '+':1,'-':1}

    for i in L:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            Output.append(i)
        elif i == '(':
            opstack.push(i)
        elif i == ')':
            top = opstack.pop()
            while top != '(':
                Output.append(top)
                top = opstack.pop()
        elif i in operators:
            
            for j in range(opstack.size()):
                if operators[i] >= operators[opstack.peek()]:
                    ops  = opstack.pop()
                    Output.append(ops)
            
            opstack.push(i)
        
    for i in range(opstack.size()):
        Output.append(opstack.pop())
    postfix = ''
    for i in Output:
        postfix = postfix + 1
    return postfix
                
postFix("(A + B) * C")
