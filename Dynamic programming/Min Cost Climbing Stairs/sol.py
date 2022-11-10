from typing import List

#Shit
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 0 
        res = 0
        while i < len(cost):
            if len(cost) - (i+1) == 3:
                if cost[i+2] < (cost[i+1] + cost[i+3]):
                    res += cost[i+2]
                    i+=2
                else: 
                    res += cost[i+1]
                    i+=1
            elif len(cost)-(i+1)  == 1:
                i+=2
            elif cost[i+1] < cost[i+2]:
                res+= cost[i+1]
                i+=1
            else:
                res+=cost[i+2]
                i+=2

        
        return res