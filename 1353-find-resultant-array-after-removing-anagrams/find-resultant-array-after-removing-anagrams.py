class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for i in range(1, len(words)):
            word1, word2 = Counter(words[i-1]),Counter(words[i])
            if word1 != word2:
                res.append(words[i])
        return res

