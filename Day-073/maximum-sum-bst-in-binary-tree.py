class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
                
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
                                                                
            l_isbst, l_min, l_max, l_sum = dfs(node.left)
            r_isbst, r_min, r_max, r_sum = dfs(node.right)
                                    
            if l_isbst and r_isbst and l_max < node.val < r_min:
                curr_sum = l_sum + r_sum + node.val
                self.res = max(self.res, curr_sum)
                return True, min(l_min, node.val), max(r_max, node.val), curr_sum
            return False, 0, 0, 0
        
        dfs(root)
        return self.res
