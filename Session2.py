8. String to Integer (atoi):

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        result = 0
        i = 0
        
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result


424. Longest Repeating Character Replacement:

class Solution(object):
    def characterReplacement(self, s, k):
        ""
        :type s: str
        :type k: int
        :rtype: int
        ""
        max_length = 0
        max_count = 0
        counts = {}
        left = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_count = max(max_count, counts[s[right]])


            if (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length





336. Palindrome Pairs:

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(check):
            return check == check[::-1]
        
        word_dict = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in word_dict:
                        res.append([word_dict[back], i])
                

                if j != len(word) and is_palindrome(suffix):  # j != len(word) to avoid duplicates
                    back = prefix[::-1]
                    if back != word and back in word_dict:
                        res.append([i, word_dict[back]])
        return res
