class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s : return 0

        char_map = {}
        start = 0 
        max_length = 0 

        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start :

                start = char_map[char] + 1 
            else: 
                max_length = max(max_length, end- start +1 )
            
            char_map[char] = end
        return max_length

















        