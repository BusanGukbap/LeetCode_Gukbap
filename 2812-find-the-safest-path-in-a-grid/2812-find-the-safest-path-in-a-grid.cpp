class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        int dx[] = {0, 0, -1, 1};
        int dy[] = {1, -1, 0, 0};

        vector<vector<int>> maze(n, vector<int>(n, -1));
        queue<pair<int, int>> q;

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    maze[i][j] = 0;
                    q.push({i, j});
                }
            }
        }

        while(!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            for (int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >=n || ny >= n || maze[nx][ny] != -1)
                    continue;
                
                maze[nx][ny] = maze[x][y] + 1;
                q.push({nx, ny});
            }
        }

        priority_queue<pair<int, pair<int, int>>> pq;
        vector<vector<int>> visited(n, vector<int>(n, 0));

        pq.push({maze[0][0], {0, 0}});
        visited[0][0] = 1;

        while(!pq.empty()) {
            int value = pq.top().first;
            int x = pq.top().second.first;
            int y = pq.top().second.second;
            pq.pop();
            
            if (x == n-1 && y == n-1)
                return value;

            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[nx][ny])
                    continue;
                
                visited[nx][ny] = 1;
                pq.push({min(value, maze[nx][ny]), {nx, ny}});
            }
        }

        return 0;
    }
};