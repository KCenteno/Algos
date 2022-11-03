import collections

def groupAnagrams(strs):
        answer = collections.defaultdict(list)
        # every list value
        for i in strs:
            count = [0] * 26
            # every string value in the list
            for j in i:
                count[ord(j) - ord("a")] += 1
            answer[tuple(count)].append(i)
        return answer.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))