class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        remove.update(stack)

        result = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)

        return ''.join(result)
