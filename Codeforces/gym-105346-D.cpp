#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> a(n), q(m), prefsum(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
        if(i == 0) prefsum[0] = a[0];
        else prefsum[i] = prefsum[i-1] + a[i];
    }

    for(int i = 0; i < m; i++) {
        cin >> q[i];
        if(q[i] > prefsum[n-1]) {
        	cout << -1 << endl;
        	continue;
		}
		if(q[i] == 0) {
			cout << 0 << endl;
			continue;
		}
        int ans = -1;
        int left = 0, right = n - 1;

        while(left <= right) {
            int mid = left + (right - left) / 2;
            if(prefsum[mid] >= q[i]) {
                ans = mid;
                right = mid-1; 
            } else {
                left = mid+1;
            }
        }

        if(ans == -1) cout << -1 << endl;
        else cout << ans + 1 << endl;
    }

    return 0;
}
