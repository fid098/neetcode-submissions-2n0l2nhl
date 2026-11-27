class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, std::vector<int>> graph;
        std::unordered_map<int, int> indegrees;
        std::queue<int> q;
        int coursecount {};

        for (int i {}; i < numCourses; i++){
            indegrees[i] = 0;
        }

        for (auto& entry : prerequisites){
            int before = entry[0];
            int after = entry[1];
            graph[before].push_back(after);
            indegrees[after]++;
        }

        for (auto& [key, val] : indegrees){
            if (val == 0){
                q.push(key);
            }
        }

        while (!q.empty()){
            int course = q.front();
            q.pop();

            coursecount++;
            for (const int nei : graph[course]){
                indegrees[nei]--;

                if (indegrees[nei] == 0){
                    q.push(nei);
                }
            }
        }

        return (coursecount == numCourses);
    }
};
