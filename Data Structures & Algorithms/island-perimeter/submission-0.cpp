class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        std::vector<std::vector<bool>> visited(ROWS, std::vector<bool>(COLS, false));
        std::queue<std::pair<int, int>> q;
        std::vector<std::pair<int, int>> directions {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int perimeter {};

        bool found = false;
        for (int r {}; r < ROWS && !found; r++){
            for (int c {}; c < COLS && !found; c++){
                if (grid[r][c] == 1 && visited[r][c] == false){
                    q.push({r,c});
                    visited[r][c] = true;
                    found = true;
                }
            }
        }

        while (!q.empty()){
            int n = q.size();
            for (int i {}; i < n; i++){
                auto [r, c] = q.front();
                q.pop();
                perimeter += 4;

                for (auto [dr, dc] : directions){
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS){
                        continue;
                    }

                    if (grid[nr][nc] == 1){
                        perimeter--;

                        if (visited[nr][nc] == false){
                            q.push({nr, nc});
                            visited[nr][nc] = true;
                        }
                    }
                    
                }
                
            }
        }

        

        return perimeter;
    }
};