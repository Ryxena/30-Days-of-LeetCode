# Question
"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]"""

# Solution

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n  # Mengambil mod k dengan panjang array
        
        # Balik seluruh array
        self.reverse(nums, 0, n - 1)
        # Balik bagian depan hingga k-1
        self.reverse(nums, 0, k - 1)
        # Balik bagian belakang dari k hingga akhir
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
           nums[start], nums[end] = nums[end], nums[start]
           start += 1
           end -= 1

