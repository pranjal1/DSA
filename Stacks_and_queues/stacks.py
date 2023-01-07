class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        _node = Node(data)
        _node.next = self.head
        self.head = _node

    def pop(self):
        if self.head:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
        return None

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def _traverse(self):
        cnode = self.head
        while cnode:
            print(cnode.data)
            cnode = cnode.next


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print("------------")
    st.push(4)
    st._traverse()
    print("------------")
    st.pop()
    st.pop()
    st._traverse()
