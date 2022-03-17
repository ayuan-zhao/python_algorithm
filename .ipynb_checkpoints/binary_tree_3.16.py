class Node:
    # 创建一个node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

#root = Node(10)
# root.PrintTree()

    # compare the new value with the parent node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
        # print the tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()


# 构造节点类
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

# 构造树类，给一个root根节点，然后可以添加节点


class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        # 形式参数为item,实质参数为node,在方法内使用用node
        node = Node(item)
        queue = [self.root]
        # 如果树是空的，对根节点赋值
        if self.root is None:
           self.root = node
           return
        # 对已有的节点进行层次遍历
        while queue:
            # 弹出队列的第一个元素
            cur_queue = queue.pop(0)
            # 如果左右子树都不为空，加入队列继续判断
            if cur_queue.lchild is None:
                cur_queue.lchild = node
                return
            else:
                queue.append(cur_queue.lchild)

            if cur_queue.rchild is None:
                cur_queue.rchild = node
                return
            else:
                queue.append(cur_queue.rchild)

    # def PrintTree(self):
    #     if self.lchild:
    #         self.lchild.PrintTree()
    #     print(self.data)
    #     if self.rchild:
    #         self.rchild.PrintTree()

    # 深度优先遍历
    # 对于一颗二叉树，深度优先搜索(Depth First Search)是沿着树的深度遍历树的节点，尽可能深的搜索树的分支。
    # 深度优先一般用递归，广度优先一般用队列。一般情况下能用递归实现的算法大部分也能用堆栈来实现。
    # 先序遍历，根左右
    # 中序遍历，左根右
    # 后序遍历，左右根
    # 可以画图解决
    # .........0.........
    #      /      \
    # ....1.........2.....
    #   /  \       /  \
    #..3....4.....5....6...
    # / \  /
    # 7...8.9..............

    # 层次遍历：0123456789
    # 先序遍历：0137894256
    # 有两个叉的算中，不算左
    # 中序遍历：7381940526
    # 后序遍历：7839415620
    # *********
     # .........A.........
    #       /      \
    # .....B.........F.....
    #      \       /  \
    # .......C..........G...
    #      / \        /
    # .....D...E......H.......

    # 层次遍历:ABFCGDEH
    # preorder:ABCDEFGH
    # inorder:BDCEAFHG
    # postorder:DECBHGFA


# 广度优先遍历（层次遍历）
# 利用队列实现数的层次遍历

    def breath_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem, end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

# 递归实现先序遍历：根——左——右
    def preorder(self, node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)
# 中序遍历 左——根——右

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)
# 后序遍历

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("--BFS--广度优先遍历——————")
    tree.breath_travel()
    print()
    print("------preorder-------")
    tree.preorder(tree.root)
    print()
    print("------inorder-------")
    tree.inorder(tree.root)
    print()
    print("----- postorder-----")
    tree.postorder(tree.root)
