def lengthOfLongestSubstring(s):
    hashset = set()
    l, r, res = 0, 0, 0 #initialize pointers
    for r in range(len(s)): # loop throught the string
        while s[r] in hashset: # checking for dupicates
            hashset.remove(s[l]) # do something
            l += 1  # update the pointer
        hashset.add(s[r])
        res = max(res, r - l + 1) # find res
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))