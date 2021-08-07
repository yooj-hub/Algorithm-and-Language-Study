/**
* BaekJoon 16920 확장게임
* programmer: yooj
* Date: 21.08.07
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/16920
**/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// 각 플레이어의 땅을 저장할 큐
vector<queue<tuple<int, int, int, int>>> vq(9);

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m, p; // 격자판의 크기 와 플레이어의 수를 입력 받음
    int z = 0;
    cin >> n >> m >> p;
    int s[p];
    int mx = n * m; // 최대 값
    int ans[p]; // 정답을 저장할 배열
    fill(ans, ans + p, 0);
    for (int i = 0; i < p; i++) {
        cin >> s[i]; // 각 한 턴에 화장하는 칸을 저장함
    }
    int a[n][m]; // 지도를 저장할 배열
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char t;
            cin >> t;
            if (t == '.') { // , 일경우 -1 로저장
                a[i][j] = -1;
            } else if (t == '#') {
                a[i][j] = -2; // # 일 경우 -2 로저장
                mx--;
            } else {// 숫자일 경우 숫자 그대로 저장
                a[i][j] = t - '0';
                z++;
                ans[a[i][j] - 1]++;
                vq[a[i][j] - 1].push({a[i][j], i, j, 0}); // 각 큐에 저장
            }

        }
    }
    //움직임을 나타내는 배열
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {1, -1, 0, 0};

    int turn = 0; // 현재 턴을 나타냄

    while (z != mx) {
        turn++;

        int zeroQ = 0; // 빈 큐의 개수를 나타내는 변수

        for (int i = 1; i <= p; i++) {
            if (vq[i - 1].empty()) { // 큐가 비었을 때 zeroQ를 증가시킴
                zeroQ++;
            }
            // 각 큐에 대하여 bfs 알고리즘을 진행함
            while (!vq[i - 1].empty()) {
                int c, x, y, cnt;
                tie(c, x, y, cnt) = vq[i - 1].front();

                if (cnt == s[i - 1] * turn) {
                    break;
                }
                vq[i - 1].pop();
                for (int l = 0; l < 4; l++) {
                    int nx = x + dx[l];
                    int ny = y + dy[l];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                        continue;
                    if (a[nx][ny] == -1) {
                        ans[c - 1]++;
                        z++;
                        a[nx][ny] = c;
                        vq[i - 1].push({c, nx, ny, cnt + 1});
                    }
                }
            }
        }
        if (z == mx || zeroQ == p) // 최댓값을 도달하거나 모든 큐가 비면 정지
            break;
    }
    //정답 출력
    for (int u = 0; u < p; u++) {
        cout << ans[u] << ' ';
    }
    return 0;

}
