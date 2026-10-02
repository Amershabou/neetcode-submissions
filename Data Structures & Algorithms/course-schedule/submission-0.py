class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}
        preqs = [0] * numCourses
        for c, preq in prerequisites:
            courses[preq].append(c)
            preqs[c] += 1

        taken = 0
        queue = deque([c for c in range(numCourses) if preqs[c] == 0])
        while queue:
            cur = queue.popleft()
            taken += 1
            for c in courses[cur]:
                preqs[c] -= 1
                if preqs[c] == 0:
                    queue.append(c)
        
        return numCourses == taken


        