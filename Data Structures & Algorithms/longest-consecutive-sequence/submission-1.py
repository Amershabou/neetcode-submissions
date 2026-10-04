class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = {}
        nums_set = set(nums)
        max_seq = 0
        for n in nums:
            if n in nums_map:
                continue
            c = 1
            r = n + 1
            l = n - 1
            while r in nums_set:
                nums_map[r] = True
                c += 1
                r += 1
            while l in nums_set:
                nums_map[l] = True
                c += 1
                l -= 1

            max_seq = max(max_seq, c)
        return max_seq
