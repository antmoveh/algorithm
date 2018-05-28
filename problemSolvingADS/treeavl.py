from problemSolvingADS.treebinarysearch import TreeNode, BinarySearchTree


class AVLNode(TreeNode):
    def __init__(self, key, val, left=None, right=None, parent=None):
        super().__init__(key, val, left=left, right=right, parent=parent)
        self.balanceFactor = 0
        self.leftChild: AVLNode = left
        self.rightChild: AVLNode = right
        self.parent: AVLNode = parent


class AVLTree(BinarySearchTree):

    def _put(self, key, val, currentNode: AVLNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = AVLNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = AVLNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node: AVLNode):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != node:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot: AVLNode):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        rotRoot.balanceFactor = newRoot.balanceFactor + 1 - max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot: AVLNode):
        pass

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
