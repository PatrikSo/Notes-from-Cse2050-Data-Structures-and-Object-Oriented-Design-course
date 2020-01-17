#11/1/18
#Lecture

'''
Sequential search of a function
given a list and an item, determine if the item is on the list
'''

def sequentialSearch(aList, item):
    for object in aList:
        if object == item:
            return True
        elif object > item:
            return False

    return False


l = [ 6, 9, 7, 4, 3, 1 ]
l.sort()
print(l)
print(sequentialSearch(l,5))


class HashMap:

    def __init__(self, size):
        self.size = size
        #self.slots = [None] * self.size()
        self.data = [None] * self.size

    def put(self,value):
        hashvalue = self.hashFunction(value)
        self.data[hashvalue] = value

    def hashFunction(self, value):
        return value % self.size

    def get(self, key):
        return self.data[key]

    def __getitem__(self, key):
        return self.get(key)

    def delete(self, key):
        self.data[key] = None

    def length(self):
        count = 0
        for i in self.data:
            if i != None:
                count = count + 1
        return count

    def find(self, value):
        if self.data[self.hashFunction(value)] == value:
            return True
        else:
            return False
    

h = HashMap(11)
h.put(77)
h.put(26)
h.put(93)
h.put(17)
h.put(31)
h.put(54)
print(h.get(4))
print(h.delete(10))
print(h.length())
print(h.find(31))
print(h.data)
