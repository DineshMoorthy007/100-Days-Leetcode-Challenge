def inorderTraversal(self, root):
    res = []

    def inorder (root) :
        if not root :
            return None  
                      
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res  
