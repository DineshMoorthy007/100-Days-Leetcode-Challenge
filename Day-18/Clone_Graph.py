def cloneGraph(node) :
    mapping = {}

    def clone (node) :
        if node in mapping :
            return mapping[node]
            
        copy = Node(node.val)
        mapping[node] = copy
        for n in node.neighbors :
            copy.neighbors.append(clone(n))
        return copy
        
    return clone(node) if node else None
