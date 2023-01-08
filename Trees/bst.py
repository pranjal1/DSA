class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        # O(log n)
        _node = Node(data)
        if not self.root:
            self.root = _node
            return

        cnode = self.root
        while cnode:
            if cnode.data < data:
                if not cnode.right:
                    cnode.right = _node
                    return
                cnode = cnode.right
            else:
                if not cnode.left:
                    cnode.left = _node
                    return
                cnode = cnode.left

    def lookup(self, value):
        # returns the node if match is found, else None??
        if not self.root:
            return None
        cnode = self.root
        while cnode:
            if cnode.data == value:
                return cnode
            elif cnode.data > value:
                cnode = cnode.left
            else:
                cnode = cnode.right

    def remove(self, data):
        # O(log n)
        # this has a lot of confusing steps
        # will do it later
        # https://visualgo.net/en/bst?slide=1
        pass

    def traverse(self, node):
        if not node:
            return
        print("node data --> ", node.data)
        self.traverse(node.left)
        self.traverse(node.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(100)
    bst.insert(5)
    bst.insert(150)
    bst.insert(1)
    bst.insert(7)
    bst.insert(120)
    bst.insert(170)
    bst.insert(20)
    bst.traverse(bst.root)
    print("------------------")
    bst = BST()
    bst.insert(100)
    bst.insert(150)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(20)
    bst.insert(170)
    bst.insert(120)
    bst.traverse(bst.root)
    print("------------")
    print(bst.lookup(120).data)
    print("------------")
    print(bst.lookup(121).data)
