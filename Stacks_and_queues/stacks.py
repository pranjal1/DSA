class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, data):
        _node = Node(data)
        _node.next = self.head
        self.head = _node
        self.length += 1

    def pop(self):
        if self.head:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
            self.length -= 1
        return None

    def peek(self):
        return self.head.data

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
