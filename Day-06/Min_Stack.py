class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)

        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self) :
        if self.stack[-1] == self.min[-1] :
            self.min.pop()
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min[-1]
