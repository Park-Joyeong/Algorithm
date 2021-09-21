from typing import List

"""
First Solution
--------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)-1):
            for y in range(x+1, len(nums)):
                if (nums[x]+nums[y] == target):
                    return [x, y]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}  # {} is dictionary {key:value, key:value}
        for i, num in enumerate(nums):  # i is count, num is value
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
