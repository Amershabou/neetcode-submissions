class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        preqs = [0] * numCourses
        for c, preq in prerequisites:
            courses[preq].append(c)
            preqs[c] += 1
        
        queue = deque([c for c in range(numCourses) if preqs[c] == 0])
        taken = []
        print(queue)
        while queue:
            c = queue.popleft()
            taken.append(c)

            for course in courses[c]:
                preqs[course] -= 1
                if preqs[course] == 0:
                    queue.append(course)
        
        return taken if len(taken) == numCourses else []