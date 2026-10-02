class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree_map = {i:[] for i in range(n)}

        for a, b in edges:
            tree_map[a].append(b)
            tree_map[b].append(a)
        seen = set([])
        queue = deque([0])

        while queue:
            cur = queue.popleft()
            if cur in seen:
                return False
            seen.add(cur)
            for c in tree_map[cur]:
                if c not in seen:
                   queue.append(c) 
        return len(seen) == n

        

        