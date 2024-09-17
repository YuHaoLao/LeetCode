class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        i = 1

        for i in range (len(nums)):
            if (nums[i] != nums[pointer]):
                pointer +=1 
                nums[pointer] = nums[i]
        return pointer + 1 


            
        