#include<bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> prime;
	bool isPrime[n+1];
	memset(isPrime, true, sizeof(isPrime));
	isPrime[0] = false;
	isPrime[1] = false;
	for(int p = 2; p <= n; p++) {
		if(isPrime[p]) {
			prime.push_back(p);
			for(int m = 2; m*p <= n; m++) {
				isPrime[m*p] = false;
			}
		}
	}
	
	int ans = 0;
	for(int k = 6; k <= n; k++) {
		int div = 0;
		for(int i = 0; i < prime.size(); i++) {
			if(k % prime[i] == 0) div++;
			if(div > 2) break;
		}
		if(div == 2) ans++;
	}
	
	cout << ans << endl;
	
	return 0;
}