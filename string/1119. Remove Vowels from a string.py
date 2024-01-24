class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        return ''.join([char for char in s if char not in vowels])
        
class Solution:
    def removeVowels(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] not in 'aeiou':
                result.append(s[i])
        return "".join(result)
        