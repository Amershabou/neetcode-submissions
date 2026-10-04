class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dups = {n:0 for n in nums}
        for n in nums:
            dups[n] += 1
        items = sorted(dups.items(), key=lambda x:x[1], reverse=True)
        return [n[0] for n in items[:k]]

