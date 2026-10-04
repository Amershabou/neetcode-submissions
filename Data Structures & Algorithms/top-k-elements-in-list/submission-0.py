class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dups = {n:0 for n in nums}
        for n in nums:
            dups[n] += 1
        heap = [(-item[1], item[0]) for item in list(dups.items())]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            l, n = heapq.heappop(heap)
            res.append(n)
        return res

