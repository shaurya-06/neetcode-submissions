class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]

        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[len(nums) - i - 1] * nums[i])
        
        prod = [0] * len(nums)
        for i in range(len(nums)):
            prod[i] = left[i] * right[len(nums) - i - 1]
        
        return prod