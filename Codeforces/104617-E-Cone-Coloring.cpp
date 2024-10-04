#include<bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	long long b[n], dp[n];
	for(int i = 0; i < n; i++) cin >> b[i];
	if(n == 1) {
		cout << b[0] << endl;
		return 0;
	}
	if(n == 2) {
		cout << max(b[0], b[1]) << endl;
		return 0;
	}
	dp[0] = b[0];
	dp[1] = max(b[0], b[1]);
	for(int i = 2; i < n; i++) {
		dp[i] = max(b[i]+dp[i-2], dp[i-1]);
	}
	
	cout << dp[n-1] << endl;
	
	return 0;
}