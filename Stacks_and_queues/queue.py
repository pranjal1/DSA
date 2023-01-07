class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def queue(self, data):
        _node = Node(data)
        if not self.head:
            self.head = _node
            self.tail = _node
            return
        self.tail.next = _node
        self.tail = _node

    def dequeue(self):
        if not self.head:
            return
        to_return = self.head.data
        self.head = self.head.next
        return to_return

    def peek(self):
        if self.head:
            return self.head.data
        return None


if __name__ == "__main__":
    st = Queue()
    st.queue(1)
    st.queue(2)
    st.queue(3)
    print(st.dequeue())
    print(st.peek())
    print("------------")
    print(st.dequeue())
    print("------------")
    print(st.dequeue())
    print("------------")
    print(st.dequeue())
    print("------------")
    st.queue(1)
    print(st.peek())
