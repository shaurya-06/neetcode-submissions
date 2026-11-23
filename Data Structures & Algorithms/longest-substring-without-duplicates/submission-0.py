class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
        
        if len(s) == 1:
            return 1
        
        start, end = 0, 0

        window = window = {s[0]}
        max_len = 1

        while end < len(s) - 1:
            right_char = s[end + 1]

            if right_char in window:
                window.remove(s[start])
                start += 1
            else:
                end += 1
                window.add(right_char)
                max_len = max(max_len, end - start + 1)

        return max_len
        