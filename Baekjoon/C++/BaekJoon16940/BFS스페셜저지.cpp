/**
* BaekJoon 16940 BFS 스페셜 저지
* programmer: yooj
* Date: 21.07.27
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/16940
**/



#include <iostream>
#include <vector>
#include <queue>

using namespace std;

//인접 리스트를 이용하기 위한 a
vector<int> a[100000];
// bfs 탐색을 위한 q
queue<int> q;
// 방분했는지 확인하는 check
bool check[100000];
// 어디로 부터 도착해야 하는지 기롤하는 parent
int parent[100000];
// 순서를 기록하는 order
int order[100000];
// vertex 의 개수
int n;
// 큐의 크기
int l = 1;

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n; // 정점의 개수를 입력 받음

    // edges 를 입력받음
    for (int i = 0; i < n - 1; i++) {
        int from, to;
        cin >> from >> to;
        from--;
        to--;
        a[from].push_back(to);
        a[to].push_back(from);
    }
    // 순서를 입력 받음
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        order[i] = t - 1;
    }
    // 시작은 1 인데 인덱스를 맞추기 위해 1을 뺏으므로 0에서 시작
    q.push(0);
    check[0] = true; // 0 은 들렸으므로 true
    //큐에서 1번씩 팝할 것이므로 총 n 번 수행되어야 함
    for (int i = 0; i < n; i++) {
        // n 번 이전에 큐가 비었을 경우 bfs 로 모든 점을 탐색하지 못함
        if (!q.empty()) {
            int x = q.front(); // 큐의 첫 원소를 가져옴
            if (x != order[i]) { // 순서와 동일하지 않으면 종료
                cout << "0\n";
                return 0;
            }
            q.pop();
            int cnt = 0; // 총 몇개를 팝해야 하는지 확인하는 원소
            // x 에서 시작하는 정점의 인덱스를 가진 parent 배열에 x를 저장함, vertex 의 개수를 cnt 에 더해줌
            for (int y : a[x]) {
                if (!check[y]) {
                    parent[y] = x;
                    cnt += 1;
                }
            }
            // 큐의 크기에서 order 와 기록한 parent 가 맞는 지 확인함
            for (int j = 0; j < cnt; j++) {
                // l+j>=n 이 성립할 경우 초과하여 연산 하게 되어 답이 아님
                // l+j 는 확인애야할 order 의 인덱스를 가르킴
                if (l + j >= n || parent[order[l + j]] != x) {
                    cout << "0\n";
                    return 0;
                }
                // 맞을 경우 큐에 삽입 후 들린것으로 처리
                q.push(order[l + j]);
                check[order[l + j]] = true;
            }
            l += cnt; // 큐의 크기에 더해줌
        } else { // 큐가 빈 경우
            cout << "0\n";
            return 0;
        }
    }
    cout << "1\n";


}