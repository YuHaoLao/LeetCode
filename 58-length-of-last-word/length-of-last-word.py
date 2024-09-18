class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Reverse the string and strip any trailing spaces
        s = s.strip()[::-1]
        counter = 0 
        
        for char in s:
            if char == ' ':
                break
            counter += 1
        
        return counter
        