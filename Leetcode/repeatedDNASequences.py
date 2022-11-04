def findRepeatedDnaSequences(s):
    seen, res = set(), set()

    for i in range(len(s)):
        first = s[i:i + 10]
        if first in seen: # already a dup in set1
            res.add(first)
        seen.add(first)
    return res

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
print(findRepeatedDnaSequences("AAAAAAAAAAA"))
