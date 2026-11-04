class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right  = len(heights) - 1
        maxarea = 0

        while (left < right):
            minheight  = min(heights[left],heights[right])
            area = (right - left)*minheight
            maxarea = max(area,maxarea)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            
        return maxarea