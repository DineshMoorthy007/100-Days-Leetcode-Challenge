class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        premap = { i:[] for i in range (numCourses)}
        for cr, pr in prerequisites :
            premap[cr].append(pr)

        vset = set()
        def dfs(cr) :
            if cr in vset :
                return False
            if premap[cr] == [] :
                return True

            vset.add(cr)
            for pre in premap[cr] :
                if not dfs(pre):
                    return False
            vset.remove(cr)
            premap[cr] = []
            return True
        
        for cr in range(numCourses):
            if not dfs(cr) : return False
        return True
