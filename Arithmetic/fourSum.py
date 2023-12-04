class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        '''
        :param nums: List[int]
        :param target: int
        :return: List[int]
        '''
        if len(nums) < 4:
            return []
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                now = nums[i] + nums[j]
                p = j + 1
                q = len(nums) - 1
                while p < q:
                    if nums[p] + nums[q] + now == target:
                        if (nums[i], nums[j], nums[p], nums[q]) not in ans:
                            ans.add((nums[i], nums[j], nums[p], nums[q]))
                    if nums[p] + nums[q] + now > target:
                        q -= 1
                    else:
                        p += 1
        return list(ans)
