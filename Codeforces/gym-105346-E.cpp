#include<bits/stdc++.h>
using namespace std;

typedef pair<long long, long long> pii;
int main() {
	long long n, d, x;
	cin >> n >> d >> x;
	long long k[n], c[n];
	for(int i = 0; i < n; i++) cin >> k[i];
	for(int i = 0; i < n; i++) cin >> c[i];
	
	vector<pii> v;
	for(int i = 0; i < n; i++) v.push_back(make_pair(c[i], k[i]));
	sort(v.begin(), v.end(), [](pii a, pii b) { return a.first > b.first; });
	
	long long ans = 0, takes = x*d, take;
	for(int i = 0; i < v.size(); i++) {
		if (takes) {
			take = min(takes, min(d, v[i].second));
			ans += take*v[i].first;
			takes -= take;
		}
	}

	cout << ans << endl;
	
	return 0;
}