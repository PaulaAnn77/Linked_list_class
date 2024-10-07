# Author: Paula Farebrother
# Created: July 2024
# Last modified: Oct 2024

from node_class import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, newNode):
        node = Node(newNode)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            self.size += 1
            lastNode.next = node

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            for node in self.__iter__():
                print(node)


    def search(self, data):
        for node in self.__iter__():
            if data == node:
                return True

        return False

    def count(self):
        count = self.size
        return count
        print()
        print("The number of items in the list are: ")
        print(count)

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def deleteHead(self):
        if self.isListEmpty() is True:
            print("This list is empty")
        else:
            previousHead = self.head  # head goes into temp var
            self.head = self.head.next  # next node becomes head
            previousHead.next = None  # old head pointer is deleted

    def deleteAt(self, position):
        if position < 1 or position >= self.size:
            print("Invalid position.")
            return
        if self.isListEmpty() is False:
            if position == 1:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 1  # set at 1 so exact representative position
            # can be used rather than starting at 0 for the first item in list
            while True:
                if currentPosition == position:
                    deletedNode.next = currentNode.next  # next held in temp var
                    currentNode.next = None  # pointer deleted
                    break
                deletedNode = currentNode  # becomes deleted node in temp var
                currentNode = currentNode.next  # next becomes current node
                currentPosition += 1  # moves position along until matches given
