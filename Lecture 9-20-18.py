#Data Structures: The Stack

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

def main():
    #create empty stack
    someStack = Stack()
    someStack.push("Mary")
    someStack.push("Bill")
    someStack.push("Joe")

    print('The stack has ', someStack.size(), 'items')
    
    for i in range(someStack.size()):
        print(someStack.pop())

    print('The stack has ', someStack.size(), 'items')

def parenthesesCheck(someString):
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
        return True
    else:
        return False

parenthesesCheck('((())())))))')

def removeValues(someString):
    s = ''
    for i in range(len(someString)):
        if someString[i] == '(' or someString[i] == ')':
            s = s + someString[i]

    return s

print(parenthesesCheck(removeValues('(6+9+(((5+8)-3)')))
print(parenthesesCheck("(((())"))
print(parenthesesCheck("()"))
