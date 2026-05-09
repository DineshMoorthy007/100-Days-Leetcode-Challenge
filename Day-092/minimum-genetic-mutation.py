class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
            
        if endGene not in bank:
            return -1
                            
        queue = deque([(startGene, 0)])
        visited = {startGene}
                                        
        choices = ['A', 'C', 'G', 'T']
                                                
        while queue:
            gene, steps = queue.popleft()
                                                                    
            if gene == endGene:
                return steps
                            
            gene_list = list(gene)
                                            
            for i in range(len(gene_list)):
                old = gene_list[i]
    
                for ch in choices:
                    gene_list[i] = ch
                    new_gene = ''.join(gene_list)
                                                                    
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
                                                        
                gene_list[i] = old
                                                                
        return -1
