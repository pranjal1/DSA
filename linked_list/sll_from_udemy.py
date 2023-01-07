# append
# prepend
# insert
# remove


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def traverse(self):
        cnode = self.head
        while cnode:
            print(cnode.data)
            cnode = cnode.next

    def append(self, data):
        _node = Node(data)
        self.length += 1
        if not self.head:
            self.head = _node
            self.tail = _node
            return
        self.tail.next = _node
        self.tail = _node

    def prepend(self, data):
        _node = Node(data)
        self.length += 1
        if not self.head:
            self.head = _node
            self.tail = _node
            return
        _node.next = self.head
        self.head = _node

    def insert(self, index, data):
        # O(n)
        assert index <= self.length

        cnode = self.head
        if index == 0:
            # takes care of the head thing
            self.prepend(data)
            return

        if index == self.length:
            # takes care of the tail thing
            self.append(data)
            return

        for i in range(self.length):
            if i + 1 == index:
                _node = Node(data)
                _node.next = cnode.next
                cnode.next = _node
                self.length += 1
                return
            cnode = cnode.next

    def remove(self, index):
        assert index < self.length
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        cnode = self.head
        for i in range(self.length):
            if i + 1 == index:
                if cnode.next:
                    cnode.next = cnode.next.next
                else:
                    cnode.next = None
                    self.tail = cnode
                self.length -= 1
                return
            cnode = cnode.next


if __name__ == "__main__":
    sl = SLL()
    sl.append(1)
    sl.append(2)
    sl.traverse()
    print("-------")
    sl.prepend("a")
    sl.traverse()
    print("-------")
    sl.insert(3, "new")
    sl.traverse()
    print("-------")
    sl.remove(3)
    sl.traverse()
