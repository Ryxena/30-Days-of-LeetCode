# Question
"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""

# Solution
class Solution(object):
    def majorityElement(self, nums):
        # Candidate ini nantinya untuk majority Element dan count untuk menghitung dari iterasi yang sedang berjalan
        candidate = None
        count = 0 

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

