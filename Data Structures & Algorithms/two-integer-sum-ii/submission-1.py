class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = int(len(numbers)) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif target < numbers[i] + numbers[j]:
                j-=1
            else:
                i+=1
        return list()