class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        map={0:1} #sum->frequency

        for num in nums:
            sum+=num
            if (sum-k) in map:
                count+=map[sum-k]
            map[sum]=map.get(sum,0)+1
        return count
        


        