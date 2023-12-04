class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        '''
        :param nums: list[int]
        :param val: int
        :return: int
        '''
        slow = fast = 0
        for i in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
