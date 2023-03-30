# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(s):
        if len(s) == 1:
            return s[0]
        left, first_index = 0, 0
        right = last_index = len(s)-1
        for i, c in enumerate(s):
            while right > left:
                if s[i] == s[right]:
                    left += 1
                    right -= 1
                    
        return s[first_index:last_index+1]

print(Solution.longestPalindrome("eabcbdf"))