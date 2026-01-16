def binaryTreePaths(self, root):
    res = []

    def dfs(root, cur) :
        if not root : 
            return None
                
        cur += str(root.val)

        if not root.left and not root.right :
            res.append(cur)
            return None

        cur += "->"
        dfs(root.left,cur)
        dfs(root.right,cur)

    dfs(root,"")
    return res

    # res = []

    # def dfs(root, cur, res) :
    #     if not root : 
    #         return res
                
    #     cur += "->" + str(root.val)

    #     if not root.left and not root.right :
    #         res.append(cur)
    #         return None

    #     if root.left :
    #         dfs(root.left,cur,res)

    #     if root.right :
    #         dfs(root.right,cur,res)

    # cur_path = str(root.val)

    # if not root.left and not root.right :
    #     res.append(cur_path)
    # if root.left :
    #     dfs(root.left,cur_path,res)
    # if root.right :
    #     dfs(root.right,cur_path,res)

    # return res
