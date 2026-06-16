class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left<=right:
            mid = (left + right) //2
            if self.minEatingh(mid,piles,h):
                right = mid-1
            else:
                left = mid +1
        return left

    def minEatingh(self,speed,piles,h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)
        if hours <=h:
            return True
        else:
            return False


        