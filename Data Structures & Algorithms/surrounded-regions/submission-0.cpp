class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int ROWS = board.size();
        int COLS = board[0].size();

        std::queue<std::pair<int, int>> q;
        std::vector<std::vector<bool>> visited(ROWS, std::vector<bool>(COLS, false));
        std::vector<std::pair<int, int>> directions {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for (int r {}; r < ROWS; r++) {
            for (int c {}; c < COLS; c++) {
                bool isBorder = (r == 0 || r == ROWS - 1 || c == 0 || c == COLS - 1);
                if (isBorder && board[r][c] == 'O'){ 
                    q.push({r, c});
                    visited[r][c] = true;
                }
            }
        }

        while (!q.empty()){
            int n = q.size();
            for (int i {}; i < n; i++){
                auto [r, c] = q.front();
                q.pop();

                for (auto [dr, dc] : directions){
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS || visited[nr][nc] == true || board[nr][nc] == 'X'){
                        continue;
                    }
                    if (board[nr][nc] == 'O'){
                        q.push({nr, nc});
                        visited[nr][nc] = true;
                    } 

                }
            }
        }

        for (int r {}; r < ROWS; r++){
            for (int c {}; c < COLS; c++){
                if (visited[r][c] == false && board[r][c] == 'O'){
                        board[r][c] = 'X';
                }
            }
        }
    }
};
