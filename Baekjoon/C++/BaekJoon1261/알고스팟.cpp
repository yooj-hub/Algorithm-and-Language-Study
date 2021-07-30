/**
* BaekJoon 1261
* programmer: yooj
* Date: 21.07.30
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/1261
**/

#include <iostream>
#include <deque>
#include <tuple>

using namespace std;

int a[101][101]; // 지도
bool visited[101][101]; // 방문했는지 확인하는 배열
// 움직이는 방향
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m; // n 과 m 을 입력받음
    cin >> n >> m;
    string s;
    cin.ignore();
    //지도를 입력받음
    for (int i = 0; i < m; i++) {
        getline(cin, s);
        for (int j = 0; j < n; j++) {
            a[i][j] = (int) s[j] - '0';
        }
    }
    deque<tuple<int, int, int>> q; // 튜플을 이용해서 현재위치의 행, 현재위치의 열, 현재까지 부순 벽의 수를 입력받음
    q.push_front({0, 0, 0});
    visited[0][0] = true;
    //덱을 이용한 bfs (cnt 순으로 오름차 순이 되게 함)
    while (!q.empty()) {
        int x, y, cnt;
        tie(x, y, cnt) = q.front();
        if (x == m - 1 && y == n - 1) {
            cout << cnt;
            return 0;
        }
        q.pop_front();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= m || ny >= n)
                continue;
            if (a[nx][ny] == 1 && !visited[nx][ny]) { // 벽일 경우 cnt 를 1 늘리고 맨 마지막에 추가함
                visited[nx][ny] = true;
                q.push_back({nx, ny, cnt + 1});
            } else if (a[nx][ny] == 0 && !visited[nx][ny]) { // 벽이 아닐경우 cnt 를 늘리지 않고 앞에 추가함
                visited[nx][ny] = true;
                q.push_front({nx, ny, cnt});
            }
        }
    }


}