class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in  range (0,len(nums)):
            for j in range (i+1,len(nums)):
                m = nums[i] + nums[j]
                if (target == m):
                    return[i,j]
                else:
                    pass