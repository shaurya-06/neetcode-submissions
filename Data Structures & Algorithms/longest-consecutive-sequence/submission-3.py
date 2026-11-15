class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in nums_hash:
                curr_seq_len = 1
                while num + curr_seq_len in nums_hash:
                    curr_seq_len += 1
                longest_seq = max(longest_seq, curr_seq_len)
        return longest_seq
