# Question
"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""

# Solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Pointer posisi array menggunakan k sesuai perintah
        k = 0
        # Iterasikan array nums sesuai dengan jumlah value didalmnya, bisa gunakan len
        for i in range(len(nums)):
            if nums[i] != val:
                # letakan value yang tidak sama itu pada array k yang sudah kita buat yaya
                nums[k] = nums[i]
                # Tambah value k
                k += 1

        return k

