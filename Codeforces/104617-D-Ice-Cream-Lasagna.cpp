#include<bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int R[n], G[n];
	string s;
	for(int i = 0; i < n; i++) {
		cin >> s;
		R[i] = 0;
		G[i] = 0;
		for(char c : s) {
			if(c == 'R') R[i]++;
			else G[i]++;
		}
	}
	
	int max_r = 0;
	for(int i = 0; i < n; i++) {
		if(R[i] == 0) continue;
		int temp_r = R[i];
		while(G[i+1] == 0 && i+1 < n) {
			temp_r += R[i+1];
			i++;
		}
		if(i+1 < n) temp_r += R[i+1];
		max_r = max(max_r, temp_r);
	}
	
	int max_g = 0;
	for(int i = 0; i < n; i++) {
		if(G[i] == 0) continue;
		int temp_g = G[i];
		while(R[i+1] == 0 && i+1 < n) {
			temp_g += G[i+1];
			i++;
		}
		if(i+1 < n) {
			temp_g += G[i+1];
		}
		max_g = max(max_g, temp_g);
	}
	
	cout << max(max_r, max_g) << endl;
	
	return 0;
}