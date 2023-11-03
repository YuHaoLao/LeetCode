from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        num1_dict = defaultdict(int)
        for i in range (len(nums1)):

            num1_dict[nums1[i]]+=1

        # dict to store the value in nums1
        for i in range (len(nums2)):
            if nums2[i] in num1_dict:
                if nums2[i] not in res:
                    res.append(nums2[i])
        return  res 
        # check if num2 value exsit in dict
        