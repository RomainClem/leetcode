class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #someone elses solutino 
        counts = Counter(nums)
        a = min(nums)
        b = max(nums)
        
        cur = 0
        for i in range(b, a - 1, -1):
            cur += counts[i]
            if cur >= k:
                return i
        
        return -1