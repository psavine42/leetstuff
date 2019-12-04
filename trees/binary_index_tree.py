

class BinaryIndexTree:
    def __init__(self, nums):
        self._bit = []
        self.nums = nums

        l = len(nums)
        for i in range(1, l):
            pass


    def update(self):
        pass

    def sumRange(self, i, j):
        return self._get_sum(j+1) - self._get_sum(i)


    def _get_sum(self, idx):
        pass