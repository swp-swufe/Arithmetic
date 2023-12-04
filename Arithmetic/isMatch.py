class Solution(object):
    def isMatch(self, s, p):
        '''
        :param s: str
        :param p: str
        :return: bool
        '''
        cache = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        cache[0][0] = True

        for i in range(1, len(p)):
            cache[i + 1][0] = cache[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    cache[i + 1][j + 1] = cache[i][j + 1] or cache[i - 1][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        cache[i + 1][j + 1] |= cache[i + 1][j]
                else:
                    cache[i + 1][j + 1] = cache[i][j] and (p[i] == s[j] or p[i] == '.')
        return cache[-1][-1]
