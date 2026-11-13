class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_items = len(nums)
        freqs = [[] for _ in range(num_items + 1)]
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for key, val in counts.items():
            freqs[val - 1].append(key)
        topK = []
        for i in range(0, num_items):
            if k and freqs[num_items - i - 1] != []:
                topK += freqs[num_items - i - 1]
                k -= len(freqs[num_items - i - 1])
        return topK
        