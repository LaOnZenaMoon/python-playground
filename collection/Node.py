class Node:

    nodeNext = ''
    objectValue = ''
    binHead = False
    binTail = False

    def __init__(self, nodeNext='', objectValue='', binHead=False, binTail=False):
        self.nodeNext = nodeNext
        self.objectValue = objectValue
        self.binHead = binHead
        self.binTail = binTail

    def getValue(self):
        return self.objectValue

    def setValue(self, objectValue):
        self.objectValue = objectValue

    def getNext(self):
        return self.nodeNext

    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def isHead(self):
        return self.binHead

    def isTail(self):
        return self.binTail