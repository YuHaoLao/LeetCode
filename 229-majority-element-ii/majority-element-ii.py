from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # have a list to hold answer
        res= []
        majority = defaultdict(int)
        for i in range (len(nums)):
            # append each element into dict
            majority[nums[i]]+=1
        # for each key in dict:
        for key, value in majority.items():
            #if dic.key.value > n/3:
            if value > len(nums)/3:
                #append this element into res
                res.append(key)
        return res




        