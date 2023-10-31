class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # start from 1 to len(nums):
        i = len(nums)-1
        while i > 0: 

            #  if nums[i]== nums[i-1]:
            if nums[i]== nums[i-1]:
                # nums.remove[nums[i]]
                nums.pop(i)
            i-=1
        # return len(nums)
        return len(nums)


        
        