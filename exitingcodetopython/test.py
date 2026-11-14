
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxarea = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            current_area = height * width
            maxarea = max(current_area, maxarea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxarea