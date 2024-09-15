class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two pointer solution, Complexity O(n)
        """
        l, r = 0, len(nums) - 1
        temp_nums = sorted(nums)

        while l < r:
            temp = temp_nums[l] + temp_nums[r]
            
            if temp == target:
                try:
                    l = nums.index(temp_nums[l])
                    r = nums.index(temp_nums[r], l+1, len(nums))
                except ValueError:
                    r = nums.index(temp_nums[r], 0, l+1,)
                
                return [l, r]
            
            if temp < target:
                l = l + 1
            else:
                r = r - 1