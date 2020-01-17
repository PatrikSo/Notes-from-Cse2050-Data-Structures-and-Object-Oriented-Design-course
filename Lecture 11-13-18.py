#Lecture 11/13/18
#Trees


class BinaryTree:

    #constructor
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        #if no left child, insert as left child
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        #if node has left child, push existing left child to the left
        #and insert new left child
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        #if no right child, insert as right child
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        #if node has left child, push existing left child to the left
        #and insert new left child
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    #function returns right of child of node
    def getRightChild(self):
        return self.rightChild

    #function returns left child of node
    def getLeftChild(self):
        return self.leftChild

    #function sets root value
    def setRootVal(self, obj):
        self.key = obj

    #function returns value of root
    def getRootVal(self):
        return self.key

def main():
    #create binary tree

    myTree = BinaryTree('A')
    myTree.insertLeft('X')
    myTree.insertLeft('Z')
    myTree.insertLeft('B')
    myTree.getLeftChild().getLeftChild().insertRight('M')
    myTree.insertRight('F')
    myTree.insertRight('C')
    
    print(myTree.getRootVal()) #A
    print(myTree.getLeftChild().getRootVal()) #B
    print(myTree.getLeftChild().getLeftChild().getRootVal()) #Z
    print(myTree.getLeftChild().getLeftChild().getLeftChild().getRootVal()) #X
    print(myTree.getLeftChild().getLeftChild().getRightChild().getRootVal()) #M
    print(myTree.getRightChild().getRootVal()) #C
    print(myTree.getRightChild().getRightChild().getRootVal()) #F 
    
main()
