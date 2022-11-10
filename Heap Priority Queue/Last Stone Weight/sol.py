from heapq import heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            first = -(heappop(stones))
            second = -(heappop(stones))
            if first > second:
                heappush(stones, -(first-second))

        return -(heappop(stones)) if len(stones) > 0 else 0
