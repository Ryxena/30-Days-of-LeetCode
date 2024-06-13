# Question
"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index."""

# Solution

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])

        return maxReach >= len(nums) - 1
    
# Explains
# Variable maxReach untuk menentukan jangkauan dari index saat ini, kita iterasi dalam range total array kemudian jika i > maxReach misal i = 2 dan MaxReach = 1, berarti kita tidak bisa mencapai index terakhir, return False. Jika i <= maxReach misal i = 1 dan MaxReach = 1, berarti kita bisa mencapai index terakhir, return True