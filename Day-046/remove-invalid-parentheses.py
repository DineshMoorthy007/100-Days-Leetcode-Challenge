class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance = 0
            for c in string:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        visited = set([s])
        queue = deque([s])
        result = []
        found = False
        
        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True
            
            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                next_str = curr[:i] + curr[i+1:]

                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result
