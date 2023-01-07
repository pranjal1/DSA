class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        _node = Node(data)
        if self.head:
            self.head.prev = _node
            _node.next = self.head
        self.head = _node

    def insert(self, prev_node, data):
        if prev_node is None:
            return
        _node = Node(data)
        _node.prev = prev_node
        _node.next = prev_node.next
        prev_node.next = _node
        if _node.next is not None:
            _node.next.prev = _node

    def append(self, data):
        _node = Node(data)
        if self.head is None:
            self.head = _node
            return
        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        _node.prev = cnode
        cnode.next = _node
        return

    def listprint(self, node):
        while node is not None:
            print(node.data),
            last = node
            node = node.next


if __name__ == "__main__":
    dllist = DLL()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.insert(dllist.head.next, 13)
    dllist.listprint(dllist.head)
    print("---------")
    dllist.append("last")
    dllist.listprint(dllist.head)
