def preorderTraversal(self, root):
    res = []
    stack = []

    if root :
        stack.append(root)

    while stack :
        node = stack.pop()
        res.append(node.val)
        if node.right :
            stack.append(node.right)
        if node.left :
            stack.append(node.left)

    return res

    # res = []

    # def preorder (root) :
    #     if not root :
    #         return None

    #     res.append(root.val)       
    #     preorder(root.left)
    #     preorder(root.right)

    # preorder(root)
    # return res
