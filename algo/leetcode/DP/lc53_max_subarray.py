
# https://leetcode.cn/problems/maximum-subarray/solutions/8975/hua-jie-suan-fa-53-zui-da-zi-xu-he-by-guanpengchn/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))