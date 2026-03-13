def diameterOfBinaryTree(self, root):
    self.res = 0

    def dfs (root) :
        if not root :
            return 0
            
        left = dfs(root.left)
        right = dfs(root.right)

        #unlocal res  --> this can be used when res is initialized as local variable
        self.res = max(self.res, left + right)
        return 1 + max(left ,right)
        
    dfs(root)
    return self.res
