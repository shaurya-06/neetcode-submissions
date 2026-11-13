class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            encoding = str(len(s)) + "#" + s
            result += encoding

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            delimiter = s.index("#", i)
            length = int(s[i:delimiter])

            start = delimiter + 1
            end = start + length

            result.append(s[start:end])

            i = end

        return result
