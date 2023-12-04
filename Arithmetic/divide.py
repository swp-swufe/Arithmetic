class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        :param dividend:int
        :param divisor:int
        :return:int
        '''
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else - res
