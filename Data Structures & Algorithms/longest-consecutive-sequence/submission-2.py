class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                count = 1
                x = n 
                while x + 1 in nums_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest

