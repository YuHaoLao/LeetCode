class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]] 
        for i in range(1,len(words)):
            mp1,mp2=Counter(words[i-1]),Counter(words[i]) 
            if mp1!=mp2:
                res.append(words[i]) 
        return res