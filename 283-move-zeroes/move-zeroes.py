class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder=0
        length=len(nums)
        for i in range(length):
            if nums[i]!=0:
                nums[placeholder]=nums[i]
                placeholder+=1
        while placeholder<length:
            nums[placeholder]=0
            placeholder+=1
        return nums
