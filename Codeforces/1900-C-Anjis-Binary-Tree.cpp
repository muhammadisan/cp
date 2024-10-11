#include<bits/stdc++.h>
using namespace std;

struct child {
	int left;
	int right;
};

const int INF = 1e9;

int dfs(int node, int dp[], vector<child>& v, const string& s) {
	if(dp[node] != INF) return dp[node];
	
	if(v[node].left != 0) {
		if(s[node-1] == 'L') dp[node] = dfs(v[node].left, dp, v, s);
		else dp[node] = dfs(v[node].left, dp, v, s) + 1;
	}
	if(v[node].right != 0) {
		if(s[node-1] == 'R') dp[node] = min(dp[node], dfs(v[node].right, dp, v, s));
		else dp[node] = min(dp[node], dfs(v[node].right, dp, v, s) + 1);
	}
	
	return dp[node];
}

int main() {
	int t;
	cin >> t;
	while(t--) {
		int n;
		cin >> n;
		string s;
		cin >> s;
		vector<child> v(n+1);
		int dp[n+1];
		fill(dp, dp + n+1, INF);
		int x, y;
		for(int i  = 1; i <= n; i++) {
			cin >> x >> y;
			v[i] = {x, y};
			if(x == 0 && y == 0) dp[i] = 0;
		}
		
		cout << dfs(1, dp, v, s) << endl;
	}
	
	return 0;
}