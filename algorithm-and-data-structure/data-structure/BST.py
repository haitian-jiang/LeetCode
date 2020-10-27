class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return bool(self.left)

    def has_right(self):
        return bool(self.right)

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def has_one(self):
        return self.has_left() ^ self.has_right()

    def has_two(self):
        return self.has_left() and self.has_right()

    def is_leaf(self):
        return not self.has_left() and not self.has_right()

    def maximum(self):
        ptr = self
        while ptr.has_right():
            ptr = ptr.right
        return ptr

    def minimum(self):
        ptr = self
        while ptr.has_left():
            ptr = ptr.left
        return ptr

    def __iter__(self):
        if self:
            if self.has_left():
                for node in self.left:
                    yield node
            yield self.key
            if self.has_right():
                for node in self.right:
                    yield node


def successor(node):  # return None if no successor
    if node.has_right():
        return node.right.minimum()
    parent_node = node.parent
    while parent_node is not None and node is parent_node.right:
        node = parent_node
        parent_node = node.parent
    return parent_node


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return self.size

    def __contains__(self, item):
        if self.search(item) is None:
            return False
        return True

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        out = ''
        for n in self:
            out = out + str(n) + ' '
        return out

    def search(self, k):
        ptr = self.root
        while ptr and ptr.key != k:
            if k < ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return ptr

    def insert(self, k):
        if self.root is None:  # empty tree
            self.root = TreeNode(k)
        else:
            insert_pos = self.root
            parent_pos = None
            while insert_pos:
                parent_pos = insert_pos
                if k < insert_pos.key:
                    insert_pos = insert_pos.left
                elif k > insert_pos.key:
                    insert_pos = insert_pos.right
                else:  # insert_pos.key == k
                    raise KeyError("key already exists")
            new_node = TreeNode(k, parent=parent_pos)
            if k < parent_pos.key:
                parent_pos.left = new_node
            else:  # no chance of ==. If so, raised error before
                parent_pos.right = new_node
        self.size += 1

    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError("404")
        if node.is_leaf():
            if node.is_left():
                node.parent.left = None
            elif node.is_right():
                node.parent.right = None
            else:  # delete the only root
                self.root = None
        elif node.has_one():
            if node.has_left():
                if node.is_left():
                    node.parent.left = node.left
                elif node.is_right():
                    node.parent.right = node.left
                else:  # delete root
                    self.root = node.left
                    self.root.parent = None
            else:
                if node.is_left():
                    node.parent.left = node.right
                elif node.is_right():
                    node.parent.right = node.right
                else:  # delete root
                    self.root = node.right
                    self.root.parent = None
        else:  # has two children
            suc = successor(node)
            suc.key, node.key = node.key, suc.key
            if suc.is_leaf():
                if suc.is_left():
                    suc.parent.left = None
                elif suc.is_right():
                    suc.parent.right = None
            else:  # successor must be left child and has only right subtree
                suc.parent.left = suc.right



if __name__ == '__main__':
    a = BST()
    a.insert(12)
    a.insert(5)
    a.insert(18)
    a.insert(2)
    a.insert(9)
    a.insert(15)
    a.insert(19)
    a.insert(17)
    a.insert(13)
    a.insert(14)
    print(a)
    a.delete(12)
    print(a, a.root.key, sep='\n')

