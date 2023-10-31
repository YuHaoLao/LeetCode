from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int: 
        FrequentEven = defaultdict(int)
        res=[]
        for i in range (len(nums)):
            if nums[i]%2 == 0:
                FrequentEven[nums[i]]+=1
        
        if not FrequentEven:
            return -1
        frequent = max(FrequentEven.values())
        for key, value in FrequentEven.items():
            if value == frequent:
                res.append(key)
        minimum_value = min(res)
        return minimum_value

        






                    
        