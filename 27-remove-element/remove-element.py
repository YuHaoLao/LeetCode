class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Traverse the list 
        i = len(nums)-1
        while i >= 0:
            # if nums[i] == val
            if nums[i] == val:
                #  remove nums[i]
                nums.remove(val)
            i-=1
        return len(nums)
        
        
        
        