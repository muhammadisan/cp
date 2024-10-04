#include<bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<pair<int, string>> v;
	for(int i = 0; i < n; i++) {
		int a;
		string s;
		cin >> a >> s;
		v.push_back(make_pair(a, s));
	}
	sort(v.begin(), v.end());
	
	for(int i = 0; i < v.size(); i++) {
		cout << v[i].second << " ";
	}
	cout << endl;
	
	return 0;
}