class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        global_max = 0
        while left < right:
            current_vol = min(heights[left], heights[right]) * (right - left)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
            if current_vol > global_max:
                global_max = current_vol
        return global_max