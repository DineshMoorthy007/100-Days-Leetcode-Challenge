class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.arr = nums[:]
                                
        for i in range(self.n):
            self._update(i, nums[i])

    def _update(self, i: int, delta: int) -> None:
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def update(self, i: int, val: int) -> None:
        delta = val - self.arr[i]
        self.arr[i] = val
        self._update(i, delta)

    def prefix(self, i: int) -> int:
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix(right) - self.prefix(left - 1)
