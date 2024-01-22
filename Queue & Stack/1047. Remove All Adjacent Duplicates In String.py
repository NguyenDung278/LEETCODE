from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = {2 * ch for ch in ascii_lowercase}
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d,"")
        return s
    

class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for ch in s:
            if output  and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return "".join(output)