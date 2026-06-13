class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        for i in range(0,len(nums)):
            prod.append(self.get_product_except_key(nums,i))
        return prod

    def get_product_except_key(self,nums:List[int],position) -> int:
        product = 1
        for i in range(0,len(nums)):
            if i == position:
                continue
            else:
                product = product * nums[i]
        return product
            

            