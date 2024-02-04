class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map: dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        stack_integer: int = 0

        for i in range(len(s)):
            stack_integer += (-1 if len(s) - 1 > i and roman_map[s[i]] < roman_map[s[i+1]] else 1) * roman_map[s[i]]
    
        return stack_integer

