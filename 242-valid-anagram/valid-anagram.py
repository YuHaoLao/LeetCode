class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_t =  sorted(t)
        new_s = sorted(s)
        return new_s == new_t
        