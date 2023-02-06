
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        keys = list(d.keys())
        result = 0
        for i in keys:
            while i in s:
                s = s.replace(i,"_", 1)
                result+=d[i]
        return result



a=Solution()
print(a.romanToInt("MCMXCIV"))