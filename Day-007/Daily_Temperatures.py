def dailyTemperatures(self, temperatures):

    r = [0] * len(temperatures)
    stack = []  # indices

    for i, t in enumerate(temperatures) :
        while stack and temperatures[stack[-1]] < t :
            si = stack.pop()
            r[si] = i - si
        stack.append(i)

    return r
