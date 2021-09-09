#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    int ans = -1;
    for (int i = 0; i < n; i++) {
        auto lb = lower_bound(a.begin(), a.end(), m + a[i]);
        if (lb - a.begin() == a.size()) {
            continue;
        }
        int &i1 = a[lb - a.begin()];
        int i2 = abs(i1 - a[i]);
        if (i2 < m) {
            continue;
        }
        if (ans == -1 || ans > i2)
            ans = i2;
    }
    cout << ans;
    return 0;
}