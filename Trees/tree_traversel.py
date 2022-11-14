class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class TreeTraversal:

    def inorder(self, _root):
        if _root:
            self.inorder(_root.left)
            print(_root.val, end=" ")
            self.inorder(_root.right)

    def preorder(self, _root):
        if _root:
            print(_root.val, end=" ")
            self.preorder(_root.left)
            self.preorder(_root.right)

    def postorder(self, _root):
        if _root:
            self.postorder(_root.left)
            self.postorder(_root.right)
            print(_root.val, end=" ")

    def height(self, _root):
        if _root is None:
            return 0
        else:
            left_height = self.height(_root.left)
            right_height = self.height(_root.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def current_level(self, _root, level):
        if _root is None:
            return
        if level == 1:
            print(_root.val, end=" ")
        elif level > 1:
            self.current_level(_root.left, level - 1)
            self.current_level(_root.right, level - 1)

    def level_order(self, _root):
        h = self.height(_root)
        for i in range(1, h+1):
            self.current_level(_root, i)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(7)
    root.right.right = Node(9)
    tree_traversal = TreeTraversal()

    tree_traversal.inorder(root)
    print("\n")
    tree_traversal.preorder(root)
    print("\n")
    tree_traversal.postorder(root)
    print("\n")
    print(tree_traversal.height(root))
    print("\n")
    tree_traversal.level_order(root)