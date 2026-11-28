class Solution {
private:
    std::vector<int> parent;

    int find(int x){
        if (parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unite(int x, int y){
        int rx = find(x);
        int ry = find(y);
        if (rx == ry){
            return false;
        }
        parent[rx] = ry;
        return true;
    }

public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);

        int components = n;
        for (const auto& edge : edges){
            if (unite(edge[0], edge[1])){
                components--;
            }
        }

        return components;
    }
};
