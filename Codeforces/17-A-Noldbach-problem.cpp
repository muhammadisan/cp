#include<bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
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
	for(int i = 0 ; i < prime.size()-1; i++) {
		if(prime[i] + prime[i+1] + 1 <= n) {
			if(isPrime[prime[i] + prime[i+1] + 1]) ans++;
		} else {
			break;
		}
	}
	
	if(ans >= k) cout << "YES\n";
	else cout << "NO\n";
	
	return 0;
}