def postorderTraversal(self, root):
    stack = [(root,False)]
    res = []

    while stack:
        cur ,v = stack.pop()
        if cur :
            if v : 
                res.append(cur.val)
            else :
                stack.append((cur,True))
                stack.append((cur.right,False))
                stack.append((cur.left,False))

    return res

# res = []

# def postOrder(root) :
#     if not root :
#         return None

#     postOrder(root.left)
#     postOrder(root.right)
#     res.append(root.val)

# postOrder(root)
# return res
