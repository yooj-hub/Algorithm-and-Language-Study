#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
bool d[1501][1501];

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int a, b, c;
    cin >> a >> b >> c;
    int sum = a + b + c;
    if ((sum) % 3) {
        cout << 0 << '\n';
        return 0;
    } else {
        int first, second;
        queue<pair<int, int>> q;
        q.push({a, b});
        d[a][b] = true;
        d[b][a] = true;
        int third;
        while (!q.empty()) {
            tie(first, second) = q.front();
            q.pop();
            third = sum - first - second;
            if (first == second && first == third) {
                cout << 1 << '\n';
                return 0;
            }
            if (first != second) {
                if (first > second) {
                    swap(first, second);
                }
                if (!d[first + first][second - first]) {
                    q.push({first + first, second - first});
                    d[first + first][second - first] = true;
                    d[second - first][first + first] = true;
                }
            }
            if (first != third) {
                if (first > third) {
                    swap(first, third);
                }
                if (!d[first + first][third - first]) {
                    q.push({first + first, third - first});
                    d[first + first][third - first] = true;
                    d[third - first][first + first] = true;
                }
            }
            if (second != third) {
                if (second > third) {
                    swap(second, third);
                }
                if (!d[second + second][third - second]) {
                    q.push({second + second, third - second});
                    d[second + second][third - second] = true;
                    d[third - second][second + second] = true;
                }
            }
        }
    }
    cout << 0<< '\n';
    return 0;
}