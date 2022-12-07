# recursive: foreach num, get subseq with num and without num, only include num if prev was less, 
# cache solution of each; dp=subseq length which must end with each num, curr num must be after a prev dp 
# or by itself;
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
