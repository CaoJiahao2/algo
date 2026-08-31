from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph: dict[int, list[int]] = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        seen = 0
        while q:
            u = q.popleft()
            seen += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return seen == numCourses

