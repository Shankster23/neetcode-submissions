class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.left, -num)
        elif len(self.left) == 0:
            if num <= self.right[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        elif len(self.right) == 0:
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        else:
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, -heapq.heappop(self.left))
            elif len(self.right) > len(self.left):
                heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        
        