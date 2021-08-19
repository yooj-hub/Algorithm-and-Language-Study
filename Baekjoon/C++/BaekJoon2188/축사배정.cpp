/**
* BaekJoon 2188 축사배정
* programmer: yooj
* Date: 21.08.19
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/2188
*/



#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n, m;
int d[201];  // 현재 축사에 들어간 소가 무슨소인지 확인하는 배열
vector<int> a[201];  // 각 소가 좋아하는 축사를 저장하는 배열
bool visited[201];  // 이미 소가 들어가있는지 확인하는 배열

bool dfs(int idx) { // bool 타입을 반환하는 dfs
    for (int k : a[idx]) {
        if (visited[k]) continue;  // 이미 축사에 소가 있을 경우 continue
        visited[k] = true;  // 축사에 소를 배정

        if (d[k] == 0 || dfs(d[k])) {  // 소가 없거나, 그 소가 다른 축사를 선택할 수 있을 경우 가능하다.
            d[k] = idx;
            return true;
        }
    }
    return false;
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n >> m;
    for (int i = 1; i < n + 1; i++) {
        int queries;
        cin >> queries;
        for (int j = 0; j < queries; j++) {
            int t;
            cin >> t;
            a[i].push_back(t);
        }
    }
    int ans = 0;
    for (int i = 1; i < 201; i++) {
        fill(visited + 1, visited + 201, false); // false 로 초기화를 하지 않을 경우 소를 다른 곳으로 옮기는 것에서 문제가 생긴다.
        if (dfs(i)) ans++;
    }
    cout<<ans;


}
