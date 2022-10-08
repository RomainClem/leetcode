class MedianFinder:

    def __init__(self):
        self.numbers = []
        self.sorted = False

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.sorted = False

    def findMedian(self) -> float:
        if not self.sorted: 
            self.numbers.sort()
            self.sorted = True
        if len(self.numbers) % 2 == 1:
            return self.numbers[len(self.numbers) // 2]
        return (self.numbers[(len(self.numbers)//2)-1] + self.numbers[(len(self.numbers)//2)]) / 2

def main():
    test = MedianFinder()
    test.addNum(1)
    test.addNum(2)
    ok = test.findMedian()
    print(ok)
    
main()
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()