from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
          ans.append(nums[nums[x]])
        return ans


sol = Solution()
print(sol.buildArray([0, 2, 1, 5, 3, 4]))
