#include<bits/stdc++.h>
using namespace std;

int main() {
	int n, q, x, t;
	cin >> n >> q;
	
	vector<int> dist(n, 0);
	for(int i = 0; i < n; i++) {
		cin >> x;
		dist[x]++;
	}
	int prefsum_left[n], prefsum_right[n], prefsum_sum[n];
	prefsum_left[0] = 0, prefsum_right[0] = 0, prefsum_sum[0] = 0;
	for(int i = 1; i < n; i++) {
		prefsum_left[i] = prefsum_left[i-1] + dist[i];
		prefsum_right[i] = prefsum_right[i-1] + dist[n-i];
		prefsum_sum[i] = prefsum_left[i] + prefsum_right[i];
	}
	
	for(int i = 0; i < q; i++) {
		cin >> t;
		if(t >= n) cout << -1;
		else {
			if(prefsum_sum[t] > n) cout << -1;
			else cout << prefsum_sum[t];
		}
		cout << endl;
	}
}