from Node import Node


class SingleLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0

    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)

    def insertAt(self, objectInsert, indexInsert):
        nodeNew = Node(objectValue=objectInsert)
        nodePrevious = self.get(indexInsert - 1)
        nodeNext = nodePrevious.getNext()
        nodePrevious.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, indexRemove):
        nodePrevious = self.get(indexRemove - 1)
        nodeRemove = nodePrevious.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrevious.setNext(nodeNext)
        self.size = self.size - 1

    def get(self, indexRetrieve):
        nodeReturn = self.nodeHead
        for index in range(indexRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead

        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue + ', ')

    def getSize(self):
        return self.size