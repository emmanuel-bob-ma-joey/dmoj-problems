class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #nums.sort()
        hashmap = []
        for i in range(len(nums)):
            hashmap.append([nums[i],i])
        hashmap.sort()
        print(hashmap)
        p1 = 0
        p2 = len(hashmap)-1
        
        
        sum = hashmap[p1][0]+hashmap[p2][0]
        while (sum != target):
            if sum < target:
                p1+=1
                sum = hashmap[p1][0]+hashmap[p2][0]
            elif sum > target:
                p2 -=1
                sum = hashmap[p1][0]+hashmap[p2][0]
        return [hashmap[p1][1],hashmap[p2][1]]