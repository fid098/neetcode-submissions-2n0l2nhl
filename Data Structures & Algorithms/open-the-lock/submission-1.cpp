class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        std::unordered_set<std::string> deads(deadends.begin(), deadends.end());
        std::unordered_set<std::string> visited;
        std::queue<std::string> q;
        if (deads.count("0000")){
            return -1;
        }
        q.push("0000");
        visited.insert("0000");
        int moves = 0;

        while (!q.empty()){
            int n = q.size();
            for (int i {}; i < n; i++){
                std::string num = q.front();
                q.pop();

                if (num == target){
                    return moves;
                }

                for (int i {}; i < num.size(); i++){
                    char orig = num[i];
                    if (orig == '0'){
                        num[i] = '9';
                    }
                    else{
                        num[i] = orig - 1;
                    }
                    std::string down = num;
                    if (orig == '9'){
                        num[i] = '0';
                    }
                    else{
                        num[i] = orig + 1;
                    }
                    std::string up = num;
                
                    num[i] = orig;
                    std::vector<std::string> neighbours {up, down};
                    for (std::string nei : neighbours){
                        if (deads.count(nei) || visited.count(nei)){
                            continue;
                        }
                        else{
                            q.push(nei);
                            visited.insert(nei);
                        }
                    }
                }
            }
            moves++;
        }

        return -1;
    }
};