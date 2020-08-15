class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Tree(object):
    global s
    s = ""
    def __init__(self):
        self.root = None
    def serialize(self):
        # we have to traverse tree in preorder traversaal
        self.preorder(self.root)
        print(s)
    def preorder(self,p):
        global s
        if p is None:
            s+= " "
            return
        s += p.val
        self.preorder(p.left)
        self.preorder(p.right)
        return None
    length = len(s)
    arr = s.split
    def deserialize(arr,start = 0,end = length - 1):
        if start > end:
            return None
        node = Node(arr[start])
        i = start
        while i <= end:
            if arr[i] > node.val:
                break
            i = i + 1
        node.left = deserialize(arr, start + 1, i - 1)
        node.right = deserialize(arr, i, end)
        return node
       

        
    def create_tree(self):
        self.root = Node('P')
        self.root.left= Node('Q')
        self.root.right=Node('R')
        self.root.left.left = Node('A')
        self.root.left.right = Node('B')
        self.root.right.left = Node('C')

    def display(self):
        self._display(self.root,0)
        print()
    def _display(self,p,level):
        if p is None:
            return
        self._display(p.right,level+1)
        print()

        for i in range(level):
            print("   ", end='')
        print(p.val)
        self._display(p.left,level+1)





bt = Tree()
bt.create_tree()
print("Tree is - ")
bt.display()
print('-'*40)
print("String repreasentation of tree is - ")
bt.serialize()
print('-'*40)
bt.deserialize()
print("Desrialization of string ",s,"is done Tree is -")
bt.display()



# I love to know if you have any other good way to solve this problem 🙂
# or if u find any mistake ,please  correct me ...