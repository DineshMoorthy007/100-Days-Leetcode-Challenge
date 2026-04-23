class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
            
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word
                                                        
        m, n = len(board), len(board[0])
        res = []
                                                                    
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            board[r][c] = '#'
                            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            
            board[r][c] = ch
                
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
                                       
        return res
