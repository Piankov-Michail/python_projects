import time

import graphviz as gv


class AVLTreeNode:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1
        self.value = value


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def __get_height__(node):
        return node.height if node else 0

    def __height_update__(self, node):
        node.height = max(self.__get_height__(node.left), self.__get_height__(node.right)) + 1

    def __small_left_rotate__(self, node):
        temp = node.right
        temp_left = temp.left
        temp.parent = node.parent
        node.parent = temp
        if temp_left is not None:
            temp_left.parent = node
        node.right = temp_left
        temp.left = node
        if temp.parent is not None:
            if temp.parent.right == node:
                temp.parent.right = temp
            elif temp.parent.left == node:
                temp.parent.left = temp
        else:
            self.root = temp
        self.__height_update__(node)
        self.__height_update__(temp)

    def __small_right_rotate__(self, node):
        temp = node.left
        temp_right = temp.right
        temp.parent = node.parent
        node.parent = temp
        if temp_right is not None:
            temp_right.parent = node
        node.left = temp_right
        temp.right = node
        if temp.parent is not None:
            if temp.parent.left == node:
                temp.parent.left = temp
            elif temp.parent.right == node:
                temp.parent.right = temp
        else:
            self.root = temp
        self.__height_update__(node)
        self.__height_update__(temp)

    def __large_left_rotate__(self, node):
        self.__small_right_rotate__(node.right)
        self.__small_left_rotate__(node)

    def __large_right_rotate__(self, node):
        self.__small_left_rotate__(node.left)
        self.__small_right_rotate__(node)

    def __balance_factor__(self, node):
        left = self.__get_height__(node.left) if node else 0
        right = self.__get_height__(node.right) if node else 0
        return left - right

    def __make_rotations__(self, node):
        balance_factor = self.__balance_factor__(node)
        if balance_factor == -2:
            if self.__balance_factor__(node.right) > 0:
                self.__large_left_rotate__(node)
            else:
                self.__small_left_rotate__(node)

        elif balance_factor == 2:
            if self.__balance_factor__(node.left) < 0:
                self.__large_right_rotate__(node)
            else:
                self.__small_right_rotate__(node)

    def __balance__(self, node):
        current = node
        next_parent = current.parent
        self.__height_update__(current)
        while next_parent is not None:
            current = next_parent
            next_parent = current.parent
            self.__height_update__(current)
            self.__make_rotations__(current)

    def search(self, value):
        current = self.root
        while current is not None:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return True
        return False

    def insert(self, value):
        if self.root is None:
            self.root = AVLTreeNode(value)
            return
        current = self.root
        new_node = AVLTreeNode(value)
        while current is not None:
            if value <= current.value:
                if current.left is None:
                    new_node.parent = current
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    new_node.parent = current
                    current.right = new_node
                    break
                current = current.right
        self.__balance__(current)

    def pop(self, value):
        if self.root is None:
            return
        current = self.root
        while current is not None:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                break
        if current is None:
            return
        if current is self.root and self.root.left is None and self.root.right is None:
            self.root = None
            return
        if current is self.root and self.root.right is None:
            self.root.left.parent = None
            self.root = self.root.left
            return
        if current.right is None:
            self.__pop__easy_case__(current)
        else:
            self.__pop__hard_case__(current)

    def __pop__easy_case__(self, current):
        if current.left is not None:
            current.left.parent = current.parent

        if current == current.parent.left:
            current.parent.left = current.left
        elif current == current.parent.right:
            current.parent.right = current.left
        self.__balance__(current)

    def __pop__hard_case__(self, current):
        new_current = current.right
        while new_current.left is not None:
            new_current = new_current.left
        current.value = new_current.value
        if new_current.right is not None:
            new_current.right.parent = new_current.parent

        if new_current.parent != current:
            if new_current.right is not None:
                new_current.right.parent = new_current.parent
            new_current.parent.left = new_current.right
        elif new_current.parent == current:
            if current.right.right is not None:
                current.right.right.parent = current
            current.right = current.right.right
        self.__balance__(new_current)

    def pop_min(self):
        if self.root is None:
            return
        current = self.root
        while current.left is not None:
            current = current.left
        if current == self.root:
            if current.right is None:
                self.root = None
            else:
                current.right.parent = None
                self.root = current.right
        else:
            if current.right is not None:
                current.right.parent = current.parent
            current.parent.left = current.right
        self.__balance__(current)

    def pop_max(self):
        if self.root is None:
            return
        current = self.root
        while current.right is not None:
            current = current.right
        if current == self.root:
            if current.left is None:
                self.root = None
            else:
                current.left.parent = None
                self.root = current.left
        else:
            if current.left is not None:
                current.left.parent = current.parent
            current.parent.right = current.left
        self.__balance__(current)

    @staticmethod
    def check_from_node(root: AVLTreeNode) -> bool:
        if root is None:
            return True
        left_height = AVLTree.__get_height__(root.left)
        right_height = AVLTree.__get_height__(root.right)
        if abs(left_height - right_height) <= 1 and \
                AVLTree.check_from_node(root.left) and AVLTree.check_from_node(root.right):
            return True
        return False

    def check_global(self):
        return self.check_from_node(self.root)

    @staticmethod
    def diff_from_node(root: AVLTreeNode, minimal=1e10) -> int:
        if root is None:
            return int(minimal)
        if root.left is not None:
            minimal = min(abs(root.value - root.left.value), minimal)
        if root.right is not None:
            minimal = min(abs(root.value - root.right.value), minimal)
        return min(AVLTree.diff_from_node(root.left, minimal), AVLTree.diff_from_node(root.right, minimal), minimal)

    def diff_global(self):
        return self.diff_from_node(self.root)

    def in_order(self, current):
        if current is not None:
            if current.left is None and current.right is None:
                return current.value
            if current.left is not None and current.right is not None:
                return f'{self.in_order(current.left)} {current.value} {self.in_order(current.right)}'
            if current.left is not None:
                return f'{self.in_order(current.left)} {current.value}'
            if current.right is not None:
                return f'{current.value} {self.in_order(current.right)}'

    def create_graph(self):
        dot = gv.Digraph(format='png')
        nodes, edges = [], []
        stack = [(self.root, "")] if self.root is not None else []

        while stack:
            node, label = stack.pop()
            if node:
                dot.node(str(id(node)), str(node.value))
                nodes.append((id(node), node.value))

                if node.left:
                    dot.edge(str(id(node)), str(id(node.left)))
                    edges.append((node.value, node.left.value))
                    stack.append((node.left, "L"))

                if node.right:
                    dot.edge(str(id(node)), str(id(node.right)))
                    edges.append((node.value, node.right.value))
                    stack.append((node.right, "R"))

        return dot, nodes, edges

    def render_avl_tree(self):
        dot, _, _ = self.create_graph()
        dot.render('avl_tree.gv', view=True)


if __name__ == "__main__":
    my_tree = AVLTree()
    for i in range(50):
        my_tree.insert(i)
    my_tree.render_avl_tree()
    time.sleep(1)
    for i in range(45):
        my_tree.pop(i)
    my_tree.render_avl_tree()
