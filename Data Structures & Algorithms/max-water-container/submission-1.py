class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        distance = j - i
        max_area = 0
        while i<j:
            distance = j - i 
            area = distance * min(heights[i],heights[j])
            if area > max_area:
                max_area = area
            if heights[i] > heights[j]:
                 j-=1
            else:
                i+=1
        return max_area