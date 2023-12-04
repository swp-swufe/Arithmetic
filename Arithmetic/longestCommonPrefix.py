class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        '''
        :param strs: List[str]
        :return: str
        '''
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def newLongestCommonPrefix(self, strs: list) -> str:
        '''
        :param strs: List[str]
        :return: str
        '''
        result = ''
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result
