class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numbers={k:[i,True] for i,k in enumerate(nums)}
        #print(numbers)
        for i,n in enumerate(nums):
            diff=target-n
            print(numbers.get(diff))
            if numbers.get(diff) and numbers[diff][0]!=i:
                output=[i,numbers[diff][0]]
                break
        return output    