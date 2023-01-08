# for this implement stack using array


class QueueCustom:
    def __init__(self) -> None:
        self.in_stk = []
        self.out_stk = []

    def push(self, data):
        self.in_stk.append(data)

    def pop(self):
        self._peek()
        return self.out_stk.pop()

    def peek(self):
        # value is only loaded to out_stk when it is empty, interesting!!
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self):
        return not (self.in_stk or self.out_stk)


if __name__ == "__main__":
    mq = QueueCustom()
    mq.push(1)
    mq.push(2)
    print(mq.in_stk)
    print(mq.out_stk)
    print(mq.pop())
    print(mq.in_stk)
    print(mq.out_stk)
    mq.push(3)
    print(mq.in_stk)
    print(mq.out_stk)
    print(mq.pop())
    print(mq.in_stk)
    print(mq.out_stk)
    print(mq.pop())
    print(mq.in_stk)
    print(mq.out_stk)
