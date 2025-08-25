class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i,j=0,n-1
        max_area=0

        while i<j:

            width=j-i
            h=min(height[i],height[j])
            area=width*h
            max_area=max(max_area,area)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area