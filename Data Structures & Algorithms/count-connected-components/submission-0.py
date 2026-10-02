class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set([])

        for i in range(n):
            if i not in seen:
                queue = deque([i])
                while queue:
                    cur = queue.popleft()
                    seen.add(cur)
                    for c in graph[cur]:
                        if c not in seen:
                            queue.append(c)
                count += 1
           
        return count

