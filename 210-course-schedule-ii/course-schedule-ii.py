class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        adj = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            v, u = prerequisite
            adj[u].append(v)

        def kahn_bfs_algo(n, adj):
            indegree = [0] * n
            for u in adj:
                for v in adj[u]:
                    indegree[v] += 1

            order = []
            q = deque([i for i in range(n) if indegree[i] == 0])
            while q:
                i = q.popleft()
                order.append(i)
                for neighbor in adj[i]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return order if len(order) == n else []

        return kahn_bfs_algo(numCourses, adj)