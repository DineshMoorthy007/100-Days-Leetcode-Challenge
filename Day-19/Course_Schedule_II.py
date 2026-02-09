class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        prereq = { c : [] for c in range (numCourses)}
        for cr, pr in prerequisites :
            prereq[cr].append(pr)

        result = []
        vt,cc = set(),set()
        def dfs(cr) :
            if cr in cc :
                return False
            if cr in vt :
                return True

            cc.add(cr)
            for pr in prereq[cr] :
                if dfs(pr) == False :
                    return False
                
            cc.remove(cr)
            vt.add(cr)
            result.append(cr)
            return True

        for c in range(numCourses) :
            if dfs(c) == False :
                return []

        return result
        
