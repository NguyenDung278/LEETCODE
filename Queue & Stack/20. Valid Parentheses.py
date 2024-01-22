class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(","}":"{","]":"["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return stack == []
    


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                previous_opening = stack.pop()
                if matching[previous_opening] !=c:
                    return False
        return stack == []