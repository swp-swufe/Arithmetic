class Solution:
    def letterCombinations(self, digits: str) -> list:
        '''
        :param digits:str
        :return: List[str]
        '''
        if len(digits) == 0:
            return []
        digit_map = {
            0: '0',
            1: '1',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        result = ['']
        for digit in digits:
            tmp_list = []
            for ch in digit_map[int(digit)]:
                for str in result:
                    tmp_list.append(str + ch)
            result = tmp_list
        return result
