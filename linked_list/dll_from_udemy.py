# prepend
# append
# insert
# remove


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.list_len = 0

    def prepend(self, data):
        _node = Node(data)
        if not self.head:
            self.head = _node
            self.tail = _node
            return

        self.head.prev = _node
        _node.next = self.head
        self.head = _node
        self.list_len += 1

    def append(self, data):
        _node = Node(data)
        if not self.head:
            self.head = _node
            self.tail = _node
            return

        _node.prev = self.tail
        self.tail.next = _node
        self.tail = _node
        self.list_len += 1

    def insert(self, index, data):
        assert index <= self.list_len
        _node = Node(data)
        if index == 0:
            self.prepend(data)
            return
        if index == self.list_len:
            self.append(data)
            return
        cnode = self.head
        for i in range(self.list_len):
            if i + 1 == index:
                _node.next = cnode.next
                cnode.next = _node
                self.list_len += 1
                return
            cnode = cnode.next

    def remove(self, index):
        assert index <= self.list_len

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            if self.list_len == 1:
                self.tail = None
            self.list_len -= 1
            return
        if index == self.list_len:
            self.tail = self.tail.prev
            self.tail.next = None
            self.list_len -= 1
            return

        cnode = self.head
        for i in range(self.list_len):
            if i + 1 == index:
                cnode.next = cnode.next.next
                self.list_len -= 1
                return
            cnode = cnode.next

    def traverse(self):
        cnode = self.head
        while cnode:
            print(cnode.data)
            cnode = cnode.next


if __name__ == "__main__":
    dl = DLL()
    dl.prepend(1)
    dl.prepend(2)
    dl.traverse()
    print("--------")
    dl.append("a")
    dl.append("b")
    dl.prepend(3)
    dl.traverse()
    print("--------")
    dl.insert(4, "new")
    dl.traverse()
    print("--------")
    dl.insert(3, "new")
    dl.traverse()
    print("--------")
    dl.remove(0)
    dl.traverse()
    print("--------")
    dl.remove(5)
    dl.traverse()
    print("--------")
    dl.remove(1)
    dl.traverse()
    print("--------")
