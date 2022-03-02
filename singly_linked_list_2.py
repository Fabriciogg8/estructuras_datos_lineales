# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList: 
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        lenght = 0
        while currentNode is not None:
            lenght += 1
            currentNode = currentNode.next
        return lenght

    # Method for insert new head node
    def insertHead(self, newNode):
        #auxiliar variable
        probe = self.head

        self.head = newNode
        self.head.next = probe
        del probe

    # Method for insert a node in a new position
    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            # While the position isn't found
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    # Insert node at the end
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    # Delete the last node
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def printList(self):
        if self.head is None:
            print("The list is empty")
            return 
        currentNode = self.head
        while True: 
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

# Node => data, next
# firstNode.data => Jhon firstNode.next => None
firstNode = Node("Jhon")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Lucas")
linkedList.insertEnd(thirdNode)
linkedList.printList()
print('\n')
linkedList.deleteEnd()
linkedList.printList()