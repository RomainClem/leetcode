from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            arr = log.split(" ")
            if 48 <= ord(arr[1][0]) <= 57: digits.append(log)
            else: letters.append(log)
              
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])

        return letters + digits
        


# print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))