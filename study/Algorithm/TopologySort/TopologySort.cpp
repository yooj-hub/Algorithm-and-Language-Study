#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
vector<int> vertex[100];
int TheNumberOfEdgesFromVertex[100];


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        vertex[from].push_back(to);
        TheNumberOfEdgesFromVertex[to]++;
    }
    queue<int> q;
    for (int i = 1; i < n + 1; i++) {
        if (TheNumberOfEdgesFromVertex[i] == 0) {
            q.push(i);
            cout << i << ' ';
        }
    }
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int c : vertex[cur]) {
            TheNumberOfEdgesFromVertex[c]--;
            if (TheNumberOfEdgesFromVertex[c] == 0) {
                q.push(c);
                cout<<c<<' ';
            }

        }
    }


}
/**
    7 8
    1 2
    1 5
    2 3
    2 6
    3 4
    4 7
    5 6
    6 4

 */
