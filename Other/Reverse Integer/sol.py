from filecmp import cmp


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        converted = str(x)
        if x < 0: converted = converted[1:]
        r_x = int(converted[::-1])
        if (x>0 and r_x >= 2147483647) or (x<0 and r_x >= 2147483648): return 0
        return r_x * -1 if x<0 else r_x 


woof =Solution
print(woof.reverse(123,123))