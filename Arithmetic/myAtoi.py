import re


class Solution(object):
    def myAtoi(self, s):
        '''
        :param s: str
        :return: int
        '''
        stripS = s.strip()
        if stripS == '' or stripS == '-' or stripS == '+':
            return 0
        s1 = re.match('[^\d]+', (stripS.lstrip('-').lstrip('+')))

        if s1 != None:
            return 0
        else:
            s1 = re.search('-*\+*\d+', stripS).group()
        if s1[0:2] == '--' or s1[0:2] == '-+' or s1[0:2] == '++':
            return 0
        result = int(s1)
        if result > 0:
            return 2147483647 if result > 2147483647 else result
        else:
            return -2147483648 if result < -2147483648 else result
