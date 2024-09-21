
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range (len(nums)):
            result = target - nums[i]
            if result in num_map:
                return [num_map[result], i]
            else:
                num_map[nums[i]] = i
        return []



          
