import collections
from typing import List


# Solution #1
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         ans_count = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] == nums[j]):
#                     ans_count = ans_count + 1
#         return ans_count

# Solution #2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(k * (k - 1) / 2 for k in collections.Counter(nums).values())
