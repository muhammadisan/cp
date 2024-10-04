#include<bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	int zero = 0;
	int one = 0;
	for(int i = 0; i < s.length(); i++) {
		if(i == 0) {
			if(s[i] == '0') zero++;
			else one++;
		} else {
			if(s[i] == '0' && s[i-1] == '1') zero++;
			else if(s[i] == '1' && s[i-1] == '0') one++;
		}
	}
//	cout << one << " " << zero << endl;
	cout << min(zero, one) << endl;
	
	return 0;
}