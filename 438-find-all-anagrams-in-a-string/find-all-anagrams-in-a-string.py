from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        target = sorted(p)
        for i in range (len(s)- (len(p)-1)):
            substring = sorted(s[i:i+len(p)])
            if target == substring:
                res.append(i)
        return res
            

        