class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num < pivot]

        greaterThanPivot = len(left)
        equalPivot = len(mid)

        if k <= greaterThanPivot:
            return self.findKthLargest(left, k)
        elif k > greaterThanPivot + equalPivot:
            return self.findKthLargest(right, k - greaterThanPivot - equalPivot)
        else:
            return mid[0]