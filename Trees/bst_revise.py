class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


# lookup
# insert


class BST:
    def __init__(self) -> None:
        self.root = None

    def lookup(self, data):
        if not self.root:
            return

        cnode = self.root
        while cnode:
            if cnode.data == data:
                return cnode
            elif cnode.data > data:
                cnode = cnode.left
            else:
                cnode = cnode.right
        return None

    def insert(self, data):
        _node = Node(data)
        if not self.root:
            self.root = _node
            return

        cnode = self.root
        while cnode:
            if cnode.data < data:
                if cnode.right is None:
                    cnode.right = _node
                    return
                cnode = cnode.right
            else:
                if cnode.left is None:
                    cnode.left = _node
                    return
                cnode = cnode.left

    def inorder_traverse(self, node):
        # dfs
        if not node:
            return
        self.inorder_traverse(node.left)
        print(node.data)
        self.inorder_traverse(node.right)


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
    bst.inorder_traverse(bst.root)
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
    bst.inorder_traverse(bst.root)
    print("------------")
    print(bst.lookup(120).data)
    print("------------")
    print(bst.lookup(121).data)
