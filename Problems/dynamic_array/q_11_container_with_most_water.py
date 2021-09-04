from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                x = j - i
                y = 0
                if (height[i] > height[j]):
                    y = height[j]
                else:
                    y = height[i]
                if (x*y > max_water):
                    max_water = x*y
        return max_water
