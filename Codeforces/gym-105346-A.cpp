#include<bits/stdc++.h>
using namespace std;

int main() {
	long long n, x, y;
	cin >> n;
	cin >> x >> y;
	long long a[n], b[n], minDist = 10e13, minX, minY;
	for(int i = 0; i < n; i++) {
		cin >> a[i] >> b[i];
		long long tempDist = (x-a[i])*(x-a[i]) + (y-b[i])*(y-b[i]);
		if(tempDist < minDist) {
			minDist = tempDist;
			minX = a[i];
			minY = b[i];
		} else if (tempDist == minDist) {
			if(a[i] < minX) {
				minX = a[i];
				minY = b[i];
			} else if(a[i] == minX && b[i] < minY) minY = b[i];
		}
	}
	
	cout << minX << " " << minY << endl;
	return 0;
}