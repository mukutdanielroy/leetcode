# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        char_set = set()
        max_length = 0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left +=1
        return max_length
    
print(Solution.length_of_longest_substring("abcabcbb"))
print(Solution.length_of_longest_substring("bbbbb"))
print(Solution.length_of_longest_substring("pwwkew"))

