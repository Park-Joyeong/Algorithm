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
# sum(List) => return int or float
#
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print collections.Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
#
# print collections.Counter(myList).values()
# [3, 4, 4, 2, 1]
#
# samenumber_count  pairs
# 0                 0
# 1                 0
# 2                 1
# 3                 3
# 4                 6
# => n*(n-1)/2
# I
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(int(k * (k - 1) / 2) for k in collections.Counter(nums).values())
