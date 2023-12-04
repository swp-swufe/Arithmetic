class Solution(object):
    '''
    :type s: str
    :type numRows: int
    :rtype: str
    '''

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = 2 * numRows - 2
        res = [''] * numRows
        for i, char in enumerate(s):
            x = i % n
            res[min(x, n - x)] += char
        return ''.join(res)
