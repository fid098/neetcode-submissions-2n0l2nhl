class Solution {
private:
    void dfs(int ROWS, int COLS, int r, int c, int& max_area, int& curr_area, vector<vector<int>>& grid, std::vector<std::vector<bool>>& visited){
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS){
            return;
        }
        if (visited[r][c] == true || grid[r][c] == 0){
            return;
        }

        curr_area += 1;
        max_area = std::max(curr_area, max_area);
        visited[r][c] = true;
        
        dfs(ROWS, COLS, r+1, c, max_area, curr_area, grid, visited);
        dfs(ROWS, COLS, r-1, c, max_area, curr_area, grid, visited);
        dfs(ROWS, COLS, r, c+1, max_area, curr_area, grid, visited);
        dfs(ROWS, COLS, r, c-1, max_area, curr_area, grid, visited);
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        std::vector<std::vector<bool>> visited(ROWS, std::vector<bool>(COLS, false));

        int max_area {};

        for (int r {}; r < ROWS; r++){
            for (int c {}; c < COLS; c++){
                if (visited[r][c] == false && grid[r][c] == 1){
                    int curr_area {};
                    dfs(ROWS, COLS, r, c, max_area, curr_area, grid, visited);
                }
            }
        }

        return max_area;


    }
};
