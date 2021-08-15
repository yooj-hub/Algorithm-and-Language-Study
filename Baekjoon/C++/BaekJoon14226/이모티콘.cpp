/**
* BaekJoon 14226 이모티콘
* programmer: yooj
* Date: 21.08.15
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/14226
**/

#include <iostream>
#include <queue>
#include<tuple>

using namespace std;
/**
 * // 처음은 이모티콘의 개수, 뒤는 클립보드의 개수이다
 * // 클립보드와 이모티콘의 개수가 완전히 동일한 경우는 세지 않는 식으로 구현해야 한다.
 */

bool visited[2000][1001];

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n; // 목표 개수를 입력 받음
    cin >> n;
    queue<tuple<int, int, int>> q; // 현재 개수, 클립보드의 개수, 현재 시간을 tuple 형으로 갖는 큐를 생성
    q.push({1, 0, 0});
    // bfs 의 경우 cnt 순으로 무조건 정렬이 되어있다.
    while (!q.empty()) {
        int cur, clip, cnt;
        tie(cur, clip, cnt) = q.front();
        if (cur == n) {
            cout << cnt;
            return 0;
        }
        q.pop();
        //클립보드에 복사하는 경우
        if (!visited[cur][cur]) {
            q.push({cur, cur, cnt + 1});
            visited[cur][cur] = true;
        }
        //클립보드에있는 것을 복사하는 경우
        if (cur+clip<=2000 && clip<=1000&&!visited[cur + clip][clip]) {
            q.push({cur + clip, clip, cnt + 1});
            visited[cur + clip][clip] = true;
        }
        //현재 이모티콘을 지우는 경우
        if (cur - 1 >= 0 && clip <= 1000 && !visited[cur - 1][clip]) {
            q.push({cur - 1, clip, cnt + 1});
            visited[cur - 1][clip] = true;
        }
    }


}