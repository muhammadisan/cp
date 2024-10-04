#include<bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	string s;
	cin >> s;
	int max_len = 0, count_of_2 = 0, left = 0, right = 0;
	while(right < n) {
		if(s[right] == '2') count_of_2++;
		
		while(count_of_2 > k) {
			if(s[left] == '2') count_of_2--;
			left++;
		}
		
		max_len = max(max_len, right - left + 1);
		right++;
	}
	
	cout << max_len << endl;
	
	return 0;
}