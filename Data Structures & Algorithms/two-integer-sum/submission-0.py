class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[n] = i
        

            