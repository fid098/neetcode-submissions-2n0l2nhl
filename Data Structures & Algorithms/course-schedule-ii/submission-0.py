class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)

        result = []

        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(node):
            if states[node] == 1:
                return []
            if states[node] == 2:
                return result

            states[node] = visiting

            for neighbours in g[node]:
                if not dfs(neighbours):
                    return False
            
            states[node] = visited
            result.append(node)
            return True

        for i in range(numCourses):
            if states[i] == 0:
                if not dfs(i):
                    return []
        return result