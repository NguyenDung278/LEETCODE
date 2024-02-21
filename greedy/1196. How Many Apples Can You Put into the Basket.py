class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        apples=units = 0
        for arr in weight:
            units +=arr
            if units>5000:
                break
            apples +=1
        return apples
    
import heapq
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        heapq.heapify(arr)
        apples = units = 0
        while arr and units +arr[0] <=5000:
            units +=heapq.heappop(arr)
            apples +=1
        return apples
        
