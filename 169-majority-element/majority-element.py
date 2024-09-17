from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        mid = len(nums)//2
        count = Counter(nums)
        for item, freq in count.items():
            if freq > mid:
                return item



        