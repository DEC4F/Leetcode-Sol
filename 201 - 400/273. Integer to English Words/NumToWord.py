"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.
"""
class Solution:
    
    def __init__(self):
        self.nums = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        
        self.ones = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        self.tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
    
    def numberToWords_div_and_conq(self, num: int) -> str:
        """
        T(n) = O(n) -- n is number of digits
        S(n) = O(1)
        """
        if not num:
            return "Zero"

        bil = num // 1000000000
        mil = (num - bil * 1000000000) // 1000000
        centi = (num - bil * 1000000000 - mil * 1000000) // 1000
        remainder = num - bil * 1000000000 - mil * 1000000 - centi * 1000
        
        res = ''
        if bil != 0:
            res = self.three(bil) + ' Billion'
        if mil != 0:
            res += ' ' if res else ''
            res += self.three(mil) + ' Million'
        if centi != 0:
            res += ' ' if res else ''
            res += self.three(centi) + ' Thousand'
        if remainder != 0:
            res += ' ' if res else ''
            res += self.three(remainder)
        return res
            
    def two(self, n):
        if n == 0:
            return ''
        if 0 < n < 10:
            return self.nums[n]
        if 10 <= n < 20:
            return self.ones[n]
        tenth = n // 10
        remainder = n - tenth * 10
        if remainder != 0:
            return self.tens[tenth] + ' ' + self.nums[remainder]
        return self.tens[tenth]
            
    def three(self, n):
        hundredth = n // 100
        remainder = n - hundredth * 100
        if remainder != 0 and hundredth != 0:
            return self.nums[hundredth] + ' Hundred ' + self.two(remainder)
        if remainder != 0 and hundredth == 0:
            return self.two(remainder)
        if remainder == 0 and hundredth != 0:
            return self.nums[hundredth] + ' Hundred'
