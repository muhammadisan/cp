#include<bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

void multi_bfs(vector<int> &sources, vector<vector<int>> &v, vector<long long> &dist) {
	queue<int> q;
	for(int source : sources) {
		dist[source] = 0;
		q.push(source);
	}
	
	while(!q.empty()) {
		int node = q.front();
		q.pop();
		for(int neighbor : v[node]) {
			if(dist[neighbor] == INF) {
				dist[neighbor] = dist[node] + 1;
				q.push(neighbor);
			}
		}
	}
}

int main() {
	int n, m, s, k, g;
	cin >> n >> m >> s >> k >> g;
	int x, y;
	vector<vector<int>> v(n+1);
	for(int i = 0; i < m; i++) {
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	vector<int> e(k), r(g);
	for(int i = 0; i < k; i++) cin >> e[i];
	for(int i = 0; i < g; i++) cin >> r[i];
	
	vector<long long> dist_h(n+1, INF), dist_g(n+1, INF);
	
	vector<int> h_source = {s};
	multi_bfs(h_source, v, dist_h);
	multi_bfs(r, v, dist_g);
	
	int ans = 0;
	
	for(int i = 0; i < k; i ++) {
		if(dist_h[e[i]] < dist_g[e[i]]) ans++;
	}
	
	cout << ans << endl;
	
	return 0;
}