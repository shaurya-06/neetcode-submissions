class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            key = tuple(counts)
            if key in grps:
                grps[key].append(s)
            else:
                grps[key] = [s]

        
        return list(grps.values())

        