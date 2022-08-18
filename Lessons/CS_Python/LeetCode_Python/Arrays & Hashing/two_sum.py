# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

class Solution:
    def twoSum(self, nums, target: int):
        map = {} # Val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return[map[diff], i]
            map[n] = i
        return
