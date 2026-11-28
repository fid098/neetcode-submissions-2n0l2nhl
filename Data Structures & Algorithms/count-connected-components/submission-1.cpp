class Solution {
private:
    std::unordered_map<int, int> parent;

    void add(int x){
        if (parent[x] == x){
            return;
        }
        parent[x] = x;
    }

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
        for (int i {}; i < n; i++){
            add(i);
        }

        for (auto entry : edges){
            unite(entry[0], entry[1]);
        }

        std::unordered_set<int> seen;
        for (auto [key, val] : parent){
            seen.insert(find(key));
        }
        
        return seen.size();
    }
};
