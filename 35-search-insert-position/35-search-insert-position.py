class Solution(object):
    def binary_search(self,low,high,target,nums):
        mid=(low+high)//2
        if low<=high:
            #base case
            if nums[mid]==target:
                return True,mid
            elif target>nums[mid]:
                low=mid+1
                return self.binary_search(low,high,target,nums)
            elif target<nums[mid]:
                high=mid-1
                return self.binary_search(low,high,target,nums)
        else:
            return False,mid
           
                
        
        
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #if length of list is one
        #mid equal to zero
        #target not found insert in the correct position
        length=len(nums)-1
        result=self.binary_search(0,length,target,nums)
        found=result[0]
        index=result[1]
        if  not found:
            print(index)
            print(nums[:index])
            nums=nums[1:index]+[target]+nums[index:]
            return index+1
        else:
            return index
        
        
                
                
        