class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None

    def traverse(self):
        cnode = self.head
        while cnode:
            print(cnode.data)
            cnode = cnode.next

    def insert_begining(self, data):
        _node = Node(data)
        if self.head is None:
            self.head = _node
            return
        _node.next = self.head
        self.head = _node

    def insert_end(self, data):
        _node = Node(data)
        if self.head is None:
            self.head = _node
            return

        cnode = self.head
        while cnode.next:
            cnode = cnode.next

        cnode.next = _node

    def insert_after(self, node, data):
        _node = Node(data)
        if self.head is None:
            return

        cnode = self.head
        while cnode:
            if cnode.data == node:
                _node.next = cnode.next
                cnode.next = _node
                return
            cnode = cnode.next
        raise Exception("Reference node can not be determined!")

    def delete_node(self, data):
        if self.head is None:
            return

        cnode = self.head
        while cnode.next:
            if cnode.next.data == data:
                cnode.next = cnode.next.next
                return
            cnode = cnode.next
        raise Exception("Can not find the node with the data to delete")

    def reverse_ll_bad(self):
        data_lst = []
        cnode = self.head
        while cnode:
            data_lst.append(cnode.data)
            cnode = cnode.next

        len_lst = len(data_lst)

        cnode = self.head
        for i in range(len_lst):
            cnode.data = data_lst[len_lst - i - 1]
            cnode = cnode.next

    def reverse_ll(self):
        if self.head is None:
            print("Empty LL!")
            return
        fnode = self.head
        snode = fnode.next
        if snode is None:
            print("Just one element in the LL!")
            return
        while snode:
            temp = snode.next
            snode.next = fnode
            fnode = snode
            snode = temp
        self.head.next = None
        self.head = fnode


if __name__ == "__main__":
    sll = SLL()
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n1.next = n2
    n2.next = n3
    sll.head = n1
    sll.traverse()
    print("----------")
    sll.insert_begining("start")
    sll.traverse()
    print("----------")
    sll.insert_end("end")
    sll.traverse()
    print("----------")
    sll.insert_after("b", "mid")
    sll.traverse()
    print("----------")
    sll.delete_node("mid")
    sll.traverse()
    print("----------")
    sll.reverse_ll()
    sll.traverse()
    print("----------")
    sll.reverse_ll()
    sll.traverse()
