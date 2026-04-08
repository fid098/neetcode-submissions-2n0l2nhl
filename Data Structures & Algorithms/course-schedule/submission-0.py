class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites[i] = [a, b] where if you want to take a, you must take b
        """

        #load every course in a dictionary
        #with b being the prerequisite for a
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)

        unvisited = 0
        visiting = 1
        visited = 2

        state = [unvisited] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True 
            
            # mark as visiting
            state[node] = visiting
            # recurse on neighbours
            for neighbours in g[node]:
                if not dfs(neighbours):
                    return False
            # if any neighbour has cycle → return False
            # mark as visited
            state[node] = visited
            # return True
            return True
            


        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True