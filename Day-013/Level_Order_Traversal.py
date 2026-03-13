def levelOrder(self, root):
        
    res = []
    queue = collections.deque()
    queue.append(root)

    while queue :
        level = []
        for _ in range (len(queue)) :
            node = queue.popleft()
            if node :
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level :
            res.append(level)

    return res
