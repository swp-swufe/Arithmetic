class Solution:
    def removeduplicates(self, nums: list) -> int:
        '''
        :param nums: list[int]
        :return: int
        '''
        if not nums:
            return 0
        n = len(nums)
        slow = fast = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
