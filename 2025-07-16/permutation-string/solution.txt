# Permutation in String

## Problem Description

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

```
Input: s1 = "abc", s2 = "lecabee"

Output: true

```

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

```
Input: s1 = "abc", s2 = "lecaabee"

Output: false

```

Constraints:

- 1 <= s1.length, s2.length <= 1000



### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the maximum of the lengths of the two strings.


### Hint 1

A brute force solution would be to check every substring of s2 with s1 by sorting s1 as well as the substring of s2. This would be an O(n^2) solution. Can you think of a better way? Maybe we can use the freqency of the characters of both the strings as we did in checking anagrams.


### Hint 2

We return false if the length of s1 is greater than the length of s2. To count the frequency of each character in a string, we can simply use an array of size O(26), since the character set consists of a through z (26 continuous characters). Which algorithm can we use now?


### Hint 3

We use a sliding window approach on s2 with a fixed window size equal to the length of s1. To track the current window, we maintain a running frequency count of characters in s2. This frequency count represents the characters in the current window. At each step, if the frequency count matches that of s1, we return true.

## Solution

```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        for letter in s1:
            s1Dict[letter] = s1Dict.get(letter, 0) + 1
        # asd
        # as
        s2Dict = {}
        l = 0
        for r in range(len(s2)):
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
            if (r - l >= len(s1)):
                s2Dict[s2[l]] = s2Dict.get(s2[l], 0) - 1
                if (s2Dict[s2[l]] == 0):
                    del s2Dict[s2[l]]
                l += 1
            if (s1Dict == s2Dict):
                return True
        return False
        

        # abc 
        # lecabee
        # create a dict out of s1 (letter to count)
        # iter thru the s2, if we have a count that exceeds dict letter count
        # then increase left pointer and subtract the old letters and keep going 
        # thru the str and until all counts are less than or equal to the counts
        # in original
        # if s1 dict == s2 dict that we get return true
        # if the loop reaches the end, the return false
        # r - l pointer needs to be less than s1 len
```