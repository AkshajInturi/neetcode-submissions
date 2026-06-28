class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left<=right:
            mid = (left+right)//2
            if self.minEatingSpeedh(mid,piles,h):
                right = mid-1
            else:
                left = mid+1
        return left


    def minEatingSpeedh(self,speed,piles,h):
        hours = 0
        for pile in piles:
            hours+=math.ceil(pile/speed)
        if hours <= h:
            return True
        else:
            return False