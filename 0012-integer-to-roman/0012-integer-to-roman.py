class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        result += 'M'*(num//1000)
        num %= 1000
        if num >= 900:
            result += 'CM'
        elif num >= 500:
            result += 'D'+'C'*(num//100-5)
        elif num >= 400:
            result += 'CD'
        else:
            result += 'C'*(num//100)
        num %= 100
        if num >= 90:
            result += 'XC'
        elif num >= 50:
            result += 'L'+'X'*(num//10-5)
        elif num >= 40:
            result += 'XL'
        else:
            result += 'X'*(num//10)
        num %= 10
        if num == 9:
            result += 'IX'
        else:
            if num>=5:
                result += 'V'
                num-=5
            result += 'IV' if num == 4 else 'I'*num
        return result