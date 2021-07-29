/**
* BaekJoon 13459 숨바꼭질 3
* programmer: yooj
* Date: 21.07.27
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/13459
**/
#include <iostream>
#include <queue>

#define MX 100000  // 최대 위치는 100000 이다.

using namespace std;
bool visited[MX + 1]; // 100000 을 기록하기위해 +1 을 더해서 설정

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k; // n에 수빈이의 위치 k 에 동생의 위치
    queue<pair<int, int>> q;  // 현재의 위치와 시간을 pair 를 통해 기록
    q.push(make_pair(n, 0));
    visited[n] = true; // 시작 위치를 방문 처리
    // BFS
    while (!q.empty()) {
        int now = q.front().first;
        int cnt = q.front().second;
        if (now == k) {
            break;
        }
        q.pop();
        int t = now;
        while (0 < t && t < k && t * 2 <= MX) {  // 큐에 순차적으로 넣기 위하여 0 초 연산을 먼저함
            if (!visited[t * 2]) {
                visited[t * 2] = true;
                q.push({t * 2, cnt});
            }
            t *= 2;

        }
        if (now + 1 <= MX && !visited[now + 1]) {
            visited[now + 1] = true;
            q.push({now + 1, cnt + 1});
        }
        if (now - 1 <= MX && now - 1 >= 0 && !visited[now - 1]) {
            visited[now - 1] = true;
            q.push({now - 1, cnt + 1});
        }
    }
    cout << q.front().second << '\n';
}

