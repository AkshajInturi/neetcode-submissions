class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if nums[pivot] <=target <=nums[-1]:
            return self.rotated_search(nums,pivot,len(nums)-1,target)
        else:
            return self.rotated_search(nums,0,pivot-1,target)
    
    def find_pivot(self,nums):
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return 0

        while left <= right:
            mid = (left + right) // 2

            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return 0

    def rotated_search(self,nums,left,right,target):
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1