#include <iostream>
#include <vector>
#include <algorithm>

#define VERTEX_MAX 101
#define INF 1000000000
using namespace std;
int d[VERTEX_MAX][VERTEX_MAX];


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n; // 점의 개수
    cin >> m; // 간선의 개수
    for (int i = 1; i < n + 1; i++) {
        fill(d[i], d[i] + n + 1, INF);
    }
    for (int i = 1; i <= n; i++) {
        d[i][i] = 0; // 자기자신은 0 으로 설정
    }
    for (int i = 0; i < m; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        if (d[from][to]<cost) continue; // 제일 낮은 값이 저장되도록 입력을 받음
        d[from][to] = cost;
    }
    //플로이드워셜 알고리즘
    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                d[a][b] = min(d[a][b], d[a][k] + d[k][b]);
            }
        }
    }
    //정답 출력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (d[i][j] == INF)
                cout << 0 << ' ';
            else
                cout << d[i][j] << ' ';
        }
        cout << '\n';
    }


}