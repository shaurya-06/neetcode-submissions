from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord("a")] += 1
            key = tuple(counts)
            grps[key].append(s)
        
        return [val for val in grps.values()]
        # grps = {}

        # for s in strs:
        #     counts = [0] * 26
        #     for char in s:
        #         counts[ord(char) - ord('a')] += 1
        #     key = tuple(counts)
        #     if key in grps:
        #         grps[key].append(s)
        #     else:
        #         grps[key] = [s]

        
        # return [value for value in grps.values()]

        