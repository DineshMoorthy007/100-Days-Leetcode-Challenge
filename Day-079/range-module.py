class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new = []
        placed = False

        for l, r in self.intervals:
            if r < left:
                new.append((l, r))
            elif right < l:
                if not placed:
                    new.append((left, right))
                    placed = True
                new.append((l, r))
            else:
                left = min(left, l)
                right = max(right, r)
        
        if not placed:
            new.append((left, right))
                                
        self.intervals = new

    def queryRange(self, left: int, right: int) -> bool:
        for l, r in self.intervals:
            if l <= left and right <= r:
                return True
        return False
        

    def removeRange(self, left: int, right: int) -> None:
        new = []
                
        for l, r in self.intervals:
            if r <= left or l >= right:
                new.append((l, r))
            else:
                if l < left:
                    new.append((l, left))
                if r > right:
                    new.append((right, r))
        
        self.intervals = new
