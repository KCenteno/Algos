def lengthOfLongestSubstring(s):
    hashset = set()
    l, r, res = 0, 0, 0
    for r in range(len(s)):
        while s[r] in hashset: # checking for dupicates
            hashset.remove(s[l])
            l += 1
        hashset.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))