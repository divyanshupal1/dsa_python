class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def __init__(self, data):
        self.head = Node(data)

    def insertAtEnd(self, data):
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = Node(data)

    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    n1 = LinkedList(10)
    n1.insertAtEnd(20)
    n1.insertAtEnd(30)
    n1.insertAtEnd(40)
    n1.print()
