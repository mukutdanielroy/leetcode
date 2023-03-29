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
        while right > left:
            if s[left] == s[right]:
                left += 1
                right -=1
                continue
            if s[left] == s[right-1]:
                last_index = right-1
                right -=1
                continue
            if s[left+1] == s[right]:
                first_index = left+1
                left +=1
                continue
            if s[left+1] == s[right-1]:
                first_index = left+1
                last_index = right-1
                right -= 1
                left += 1
                continue
        return s[first_index:last_index+1]

print(Solution.longestPalindrome("eabcb"))