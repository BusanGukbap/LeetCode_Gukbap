class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int,int>>> adj(n + 1);
        for (auto& r : roads) {
            adj[r[0]].push_back({r[1], r[2]});
            adj[r[1]].push_back({r[0], r[2]});
        }

        vector<bool> visited(n + 1, false);
        int ans = INT_MAX;

        stack<int> st;
        st.push(1);
        visited[1] = true;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            for (auto& [v, w] : adj[u]) {
                ans = min(ans, w);
                if (!visited[v]) {
                    visited[v] = true;
                    st.push(v);
                }
            }
        }
        return ans;
    }
};
