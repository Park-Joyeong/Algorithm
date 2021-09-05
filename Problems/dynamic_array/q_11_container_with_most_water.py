from typing import List

# Solution 1
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_water = 0
#         for i in range(len(height)-1):
#             for j in range(i+1, len(height)):
#                 x = j - i
#                 y = min(height[i], height[j])
#                 max_water = max(max_water, x*y)
#         return max_water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        while l < r:
            # Calculating the max area
            area = max(area, min(height[l],
                                 height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
