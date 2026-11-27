class Solution {
private:
    bool dfs(int i, std::unordered_map<int, std::vector<int>>& graph, int prevNode, std::unordered_set<int>& visited){
        //if weve seen the node before, there is a loop, so return false
        if (visited.count(i)){
            return false;
        }

        //add to set
        visited.insert(i);
        //for each of its neighbours, if the prevnode == neighbours, then keep going
        for (const int nei : graph[i]){
            if (prevNode == nei){
                continue;
            }
            //if we return false for any other neighbours, just return false 
            if (dfs(nei, graph, i, visited) == false){
                return false;
            }
        }

        return true;
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {

        //get the adjacency list for every node
        std::unordered_map<int, std::vector<int>> graph;
        for (auto& entry : edges){
            int before = entry[0];
            int after = entry[1];
            graph[before].push_back(after);
            graph[after].push_back(before);
        }

        //visited set for every node
        std::unordered_set<int> visited;
        
        //run dfs on 0 with prevnode being -1 
        return (dfs(0 , graph, -1, visited) && visited.size() == n);

    }
};
