class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        :param s: string
        :return: int
        '''
        stack = []
        ans = 0
        for i in range(len(s)):
            if stack and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
            else:
                stack.append(i)
        return ans
