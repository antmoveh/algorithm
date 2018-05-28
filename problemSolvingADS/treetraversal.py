

class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild: BinaryTree = None
        self.rightChild: BinaryTree = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        return self.key

    # 前序遍历
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


r = BinaryTree("a")
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft("b")
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight("c")
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal("hello")
print(r.getRightChild().getRootVal())


# 前序遍历 外部实现更好
def preorder(tree: BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# 后序遍历
def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild)
        postorder(tree.getRightChild)
        print(tree.getRootVal())


# 中序遍历
def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())