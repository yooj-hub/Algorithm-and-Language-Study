#include <iostream>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long d[n + 1][2];
    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            d[i][1] = 1;
            d[i][0] = 0;
        } else {
            d[i][1] = d[i - 1][0];
            d[i][0] = d[i - 1][0] + d[i - 1][1];
        }
    }
    cout << d[n][0] + d[n][1];
}