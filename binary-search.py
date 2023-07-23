class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        left = self.search(nums[:len(nums)//2],target)
        right = self.search(nums[len(nums)//2:],target)
        if left != -1:
            return left
        elif right != -1:
            return right+len(nums)//2
        else:
            return -1