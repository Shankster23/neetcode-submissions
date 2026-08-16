class Solution:
    def dist(self,coord):
        return (coord[0]**2 + coord[1]**2)**0.5
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key = self.dist)
        return points[:k]