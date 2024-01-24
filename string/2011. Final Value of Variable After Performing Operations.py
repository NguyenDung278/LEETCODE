class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        ans = 0
        for c in operations:
            if c =="++X" or c== "X++":
                ans+=1
            elif c =="--X" or c=="X--":
                ans-=1
        return ans
    

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        ans = 0
        for c in operations:
            if "+" in c:
                ans+=1
            elif "-" in c:
                ans-=1
        return ans