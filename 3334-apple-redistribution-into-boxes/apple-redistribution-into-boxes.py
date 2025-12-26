class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum=sum(apple)
        capacity.sort(reverse=True)
        

        total = 0
        boxes = 0
        for cap in capacity:
            total += cap
            boxes +=1

            if total >= apple_sum:
                return boxes
            