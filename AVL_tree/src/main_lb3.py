def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1

def balance_factor(node):
    return get_height(node.right) - get_height(node.left)

def small_right_rotate(node):
    left = node.left
    left_right = left.right
    left.right = node
    node.left = left_right
    update_height(node)
    update_height(left)
    return left

def small_left_rotate(node):
    right = node.right
    right_left = right.left
    right.left = node
    node.right = right_left
    update_height(node)
    update_height(right)
    return right

def __balance__(node):
    b_f = balance_factor(node)
    if b_f == -2:
        if balance_factor(node.left) <= 0:
            return small_right_rotate(node)
        else:
            node.left = small_left_rotate(node.left)
            return small_right_rotate(node)
    elif b_f == 2:
        if balance_factor(node.right) >= 0:
            return small_left_rotate(node)
        else:
            node.right = small_right_rotate(node.right)
            return small_left_rotate(node)
    return node

def insert(val, node: Node) -> Node:
    if not node:
        return Node(val)
    if val <= node.val:
        node.left = insert(val, node.left)
    elif val > node.val:
        node.right = insert(val, node.right)

    update_height(node)
    return __balance__(node)