class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num]+=1
        hashMap_sorted = sorted(hashMap.items(),
                            key = lambda x : x[1],
                            reverse = True)
        final_list = []
        for i in range(0,k):
            final_list.append(hashMap_sorted[i][0])
        return final_list
            
        