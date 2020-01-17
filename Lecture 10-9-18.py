#Queues & Dequeues

#class implementation of a Queue

class Queue:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#making a method for the Josephus Problem
def josephus(l):
    soldierList = Queue()
    for i in l:
        soldierList.enqueue(i)

    while soldierList.size() > 1:
        x = soldierList.dequeue()
        soldierList.enqueue(x)
        soldierList.dequeue()

    return soldierList.dequeue()

#making a variant that allows you to skip over people in killings
def josephusSkip(l, skip):
    soldierList = Queue()
    for i in l:
        soldierList.enqueue(i)

    while soldierList.size() > 1:
        for i in range(skip):
            x = soldierList.dequeue()
            soldierList.enqueue(x)
        soldierList.dequeue()

    return soldierList.dequeue()


def main():
    #simple queue tests
    q = Queue()
    print('The queue currently has: ',q.size(), ' elements')
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print('The queue currently has: ',q.size(), ' elements')
    q.dequeue()
    print('The queue currently has: ',q.size(), ' elements')
    print(q.items)

    #josephus method tests
    print(josephus([1, 2, 3, 4, 5, 6, 7]))
    print(josephus([1, 2, 3, 4, 5, 6, 7, 8]))

    #original josephus problem
    l = []
    for i in range(1,42):
        l.append(i)
    print(josephus(l))

    #new variant, lets us skip n number of people per kill
    l = []
    for i in range(1,42):
        l.append(i)
    print(josephusSkip(l,3))

    #testing with a list of names
    l = ['John', 'Peter', 'Abraham', 'Helen', 'Gloria', 'Francis']
    print(josephusSkip(l,2))

main()


