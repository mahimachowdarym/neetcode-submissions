class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2 !=0:
            return False
        target=total/2
        result={0}
        for i in nums:
            new={0}
            for r in result:
                if r+i==target:
                    return True
                if r+i<target:
                    new.add(r+i)
            result.update(new)
        return False
        