#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int a[100000];

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);
    int ans = INT32_MAX;
    int left = 0;
    int right = 0;
    int diff = 0;
    while (left < n - 1 && right < n - 1) {
        if (diff <= m) {
            diff -= a[right];
            diff += a[++right];
        } else {
            diff += a[left];
            diff -= a[++left];
        }
        if (diff >= m) {
            ans = min(diff, ans);
        }
    }
    cout << ans;

    return 0;
}