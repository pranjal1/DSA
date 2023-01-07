class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None  # next is always None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        start = self.head
        while start:
            print(start.value)
            start = start.next

    def insert_begining(self, value):  # O(1)
        _node = Node(value)
        if self.head is None:
            self.head = _node
        _node.next = self.head
        self.head = _node

    def insert_last(self, value):  # O(n)
        _node = Node(value)
        if self.head is None:
            self.head = _node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = _node

    def insert_after(self, node, value):
        if node is None:
            raise Exception("The node after which to insert does not exist!")
        _node = Node(value)
        _node.next = node.next
        node.next = _node

    def remove_node(self, value):
        start = self.head
        if start.value == value:
            self.head = self.head.next
            return
        while start.next:
            if start.next.value == value:
                if start.next.next:
                    start.next = start.next.next
                else:
                    start.next = None
                break


if __name__ == "__main__":
    SL = SinglyLinkedList()
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node(1)
    SL.head = n1
    n1.next = n2
    n2.next = n3
    SL.printList()
    print("---------")

    SL.insert_begining("start")
    SL.printList()
    print("---------")

    SL.insert_last("end")
    SL.printList()
    print("---------")

    SL.insert_after(SL.head, "between")
    SL.printList()
    print("---------")

    SL.remove_node("between")
    SL.printList()
    print("---------")
