def hasPathSum(self, root, targetSum):

    def dfs(root, cur) :
        if not root :
            return False
            
        cur += root.val

        if not root.left and not root.right :
            return cur == targetSum
            
        return (dfs(root.left, cur) or dfs(root.right, cur))

    return dfs(root, 0)   
