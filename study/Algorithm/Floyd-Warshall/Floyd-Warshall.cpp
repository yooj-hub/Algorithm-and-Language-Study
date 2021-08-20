#include <iostream>
#include <vector>
#include <algorithm>

#define INF 1000000000
using namespace std;
int d[100][100];


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n;
    cin>>m;
    for (int i = 1; i < n + 1; i++) {
        fill(d[i], d[i] + n + 1, INF);
    }
    for (int i = 1; i <= n; i++) {
        d[i][i] = 0;
    }
    for (int i = 0; i < m; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        d[from][to] = cost;
    }
    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                d[a][b] = min(d[a][b], d[a][k] + d[k][b]);
            }
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cout<<d[i][j]<<' ';
        }
        cout << '\n';
    }


}
/**
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
*/