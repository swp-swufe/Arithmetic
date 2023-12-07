def lower_bound(nums: list, target: int) -> int:
    '''
    :param nums: list[int]
    :param target: int
    :return: list[int]
    '''
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        '''
        :param nums:list[int]
        :param target: int
        :return: list[int]
        '''
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
