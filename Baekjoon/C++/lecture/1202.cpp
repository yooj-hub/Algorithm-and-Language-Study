#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct jewel {
    int v;
    int m;
};

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<jewel> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].m >> a[i].v;

    }
    sort(a.begin(), a.end(), [](jewel u, jewel v) {
        return u.v > v.v;
    });
    long long ans = 0;
    multiset<int> s;
    for (int i = 0; i < k; i++) {
        int t;
        cin >> t;
        s.insert(t);
    }
    for (int i = 0; i < n; i++) {
        auto it = s.lower_bound(a[i].m);
        if (it != s.end()) {
            ans += a[i].v;
            s.erase(it);
        }
    }
    cout << ans << '\n';
}