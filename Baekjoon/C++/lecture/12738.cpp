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
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        auto it = lower_bound(a.begin(), a.end(), t);
        if (it == a.end()) {
            a.push_back(t);
        } else {
            *it = t;
        }
    }
    cout<< a.size();

}