# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
