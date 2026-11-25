class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        std::unordered_map<int, int> outgoing;
        std::unordered_map<int, int> incoming;

        for (int i {1}; i <= n; i++){
            outgoing[i] = 0;
            incoming[i] = 0;
        }

        for (int i {}; i < trust.size(); i++){
            int trustee = trust[i][0];
            int trusted = trust[i][1];

            outgoing[trustee]++;
            incoming[trusted]++;
        }

        for (int i {}; i < outgoing.size(); i++){
            if (outgoing[i] == 0 && incoming[i] == n - 1){
                return i;
            }
        }

        return -1;
    }
};