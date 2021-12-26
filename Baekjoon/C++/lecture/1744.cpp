#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a;
    vector<int> b;
    int one = 0;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        if (t == 1){one++;continue;}

        t > 0 ? a.push_back(t) : b.push_back(t);
    }
    sort(a.begin(), a.end(), [](int u, int v) {
        return u > v;
    });
    sort(b.begin(), b.end());
    int ans = 0;
    int i = 0;
    int j = 0;
    while (!a.empty() && i < a.size() - 1) {
        ans += a[i] * a[i + 1];
        i += 2;
    }
    if (i == a.size() - 1) {
        ans += a[i];
    }
    while (!b.empty() && j < b.size() - 1) {
        ans += b[j] * b[j + 1];
        j += 2;
    }
    if (j == b.size() - 1) {
        ans += b[j];
    }
    cout << ans + one;
}