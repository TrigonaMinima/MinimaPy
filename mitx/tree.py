# Binary Tree

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value

    def getParent(self):
        return self.parent

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def __str__(self):
        return self.value

n0 = BinaryTreeNode(0)
n1 = BinaryTreeNode(1)
n2 = BinaryTreeNode(2)
n3 = BinaryTreeNode(3)
n4 = BinaryTreeNode(4)
n5 = BinaryTreeNode(5)
n6 = BinaryTreeNode(6)
n0.setLeftBranch(n1)
n0.setLeftBranch(n2)
n1.setParent(n0)
n2.setParent(n0)
n1.setLeftBranch(n3)
n1.setRightBranch(n4)
n3.setParent(n1)
n4.setParent(n1)
n2.setLeftBranch(n5)
n2.setRightBranch(n6)
n5.setParent(n2)
n6.setParent(n2)
