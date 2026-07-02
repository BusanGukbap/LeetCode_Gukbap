#include <bits/stdc++.h>

class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};

        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> maze(m, vector<int>(n, -1));
        
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>> > pq;
        pq.push({grid[0][0], {0, 0}});

        while (!pq.empty()) {
            int value = pq.top().first;
            int x = pq.top().second.first;
            int y = pq.top().second.second;

            pq.pop();
            
            if (value >= health)
                continue;

            if (x == m-1 && y == n - 1)
                break;

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= m || ny >= n)
                    continue;

                int nvalue = value + grid[nx][ny];
                if (nvalue >= health)
                    continue;
                
                if (maze[nx][ny] != -1 && maze[nx][ny] <= nvalue)
                    continue;
                
                maze[nx][ny] = nvalue;
                
                pq.push({nvalue, {nx, ny}});
            }
        }

        if (health > maze[m-1][n-1] && maze[m-1][n-1] != -1)
            return true;
        else
            return false;
    }
};