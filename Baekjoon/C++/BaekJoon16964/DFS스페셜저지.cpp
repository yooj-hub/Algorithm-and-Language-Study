/**
* BaekJoon 16964 DFS 스페셜 저지
* programmer: yooj
* Date: 21.07.27
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/16964
**/


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
// 방문했는지 확인하는 check
bool check[100000];
// 인접 리스틀 기록할 a
vector<int> a[100000];
//o 는 정답을 기록할 vector
vector<int> o;

//dfs 탐색 알고리즘
void dfs(int idx) {
    check[idx] = true;
    o.push_back(idx);
    for (int i : a[idx]) {
        if (!check[i]) {
            dfs(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int from, to;
        cin >> from >> to;
        from--;
        to--;
        a[from].push_back(to);
        a[to].push_back(from);
    }
    // b 에 순서를 기록
    vector<int> b(n);
    // order 에 해당 인덱스가 탐색되어야 할 순서를 기록
    vector<int> order(n);
    for (int i = 0; i < n; i++) {
        cin >> b[i];
        b[i]--;
        order[b[i]] = i;
    }
    // 탐색 되어야 할 순서대로 a 에 연결된 vertex 의 순서를 바꿔줌
    for (int i = 0; i < n; i++) {
        sort(a[i].begin(), a[i].end(), [&](const int &u, const int &v) {
            return order[u] < order[v];
        });
    }
    dfs(0); // 탐색
    if (b == o)
        cout << "1\n";
    else {
        cout << "0\n";
    }
    return 0;

}