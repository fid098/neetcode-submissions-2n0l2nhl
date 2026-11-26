class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();

        std::queue<std::pair<int, int>> q;
        std::vector<std::vector<bool>> visited(ROWS, std::vector<bool>(COLS, false));

        std::vector<std::pair<int, int>> directions{{1,0}, {0,1}, {-1, 0}, {0,-1}};

        for (int r {}; r < ROWS; r++){
            for (int c {}; c < COLS; c++){
                if (grid[r][c] == 0 && visited[r][c] != true){
                    q.push({r, c});
                    visited[r][c] = true;
                }
            }
        }

        int distance = 1;
        while (!q.empty()){
            int n = q.size();
            for (int i {}; i < n; i++){
                auto [r, c] = q.front();
                q.pop();

                for (auto [dr, dc] : directions){
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr < 0 || nc < 0 || nr >= ROWS || nc >= COLS || visited[nr][nc] == true || grid[nr][nc] == -1){
                        continue;
                    }

                    grid[nr][nc] = distance;
                    visited[nr][nc] = true;
                    q.push({nr, nc});
                }
            }
            distance += 1;
        }
    }
};
