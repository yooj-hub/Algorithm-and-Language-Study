/**
* BaekJoon 15558 점프게임
* programmer: yooj
* Date: 21.08.15
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/15558
**/

#include <iostream>
#include <queue>
#include <tuple>


using namespace std;

string a[2];//맵을 저장할 변수
bool visited[2][100001];// 중복을 체크하기위한 변수

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, k;//길이와 점프할 수 있는 거리를 입력 받음
    cin >> n >> k;
    cin.ignore();
    //맵을 입력 받음
    getline(cin, a[0]);
    getline(cin, a[1]);
    queue<tuple<int, int, int>> q;// 현재 위치와 지금까지 진행된 시간을 튜플형 자료구조로 가지는 큐
    q.push({0, 0, 0});
    // 움직이는 방향
    int dy[4] = {-1, 1, k, k};
    int dx[4] = {0, 0, 1, -1};
    // 처음 시작하는 곳을 방문 처리
    visited[0][0] = true;
    while (!q.empty()) {
        int x, y, cnt;
        tie(x, y, cnt) = q.front();
        //시간에 따라 안전한 곳을 지우는 연산
        a[0][cnt] = '0';
        a[1][cnt] = '0';
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= 2) {
                continue;
            }
            //n 이상일 경우 종료이므로 게임 종료
            if (ny >= n) {
                cout << "1\n";
                return 0;
            }
            // 위험한 공간은 갈 수 없다.
            if (a[nx][ny] == '0')
                continue;
            // 방문하지 않은 곳을 방문 처리
            if (!visited[nx][ny]) {
                q.push({nx, ny, cnt + 1});
                visited[nx][ny] = true;
            }

        }

    }
    cout<<"0\n";
    return 0;


}