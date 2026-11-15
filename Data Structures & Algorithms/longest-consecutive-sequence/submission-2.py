class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        longest_seq = 0
        for num in nums:
            if num + 1 in nums_hash:
                continue
            len_curr_seq = 1
            while num - 1 in nums_hash:
                len_curr_seq += 1
                num -= 1
            longest_seq = max(longest_seq, len_curr_seq)
        return longest_seq
