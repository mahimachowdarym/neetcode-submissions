class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]
        suffix=[1]
        for i in range(1,n):
            prefix.append(prefix[i-1]*nums[i-1])
        for i in range(n-2,-1,-1):
            suffix.append(suffix[n-2-i]*nums[i+1])
        res=[]
        for i in range(0,n):
            res.append(prefix[i]*suffix[n-1-i])
        return res


        