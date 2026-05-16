class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        adj = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            v, u = prerequisite
            adj[u].append(v)

        def kahn_bfs_algo(n, adj):
            indegree = [0] * n
            for u in adj:
                for v in adj[u]:
                    indegree[v] += 1

            q = deque([i for i in range(n) if indegree[i] == 0])
            order = []

            while q:
                node = q.popleft()
                order.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return order if len(order) == n else []

        order = kahn_bfs_algo(numCourses, adj)
        return len(order) > 0