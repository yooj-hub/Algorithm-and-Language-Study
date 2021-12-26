#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    vector<int> num;
    vector<int> sign;
    bool minus = false;
    int cur = 0;
    sign.push_back(1);
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '+' || s[i] == '-') {
            if (s[i] == '+') {
                sign.push_back(1);
            } else {
                sign.push_back(-1);
            }
            num.push_back(cur);
            cur = 0;
        } else {
            cur = cur * 10 + (s[i] - '0');
        }
    }
    num.push_back(cur);
    int ans = 0;
    for (int i = 0; i < num.size(); i++) {
        if (sign[i] == -1) {
            minus = true;
        }
        if (minus) {
            ans -= num[i];
        } else {
            ans += num[i];
        }
    }
    cout << ans << '\n';
}