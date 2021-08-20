#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;
int parent[100];


int findParent(int x) {
    if (parent[x] == x)return parent[x];
    return findParent(parent[x]);
}

void unionParent(int a, int b) {
    a = findParent(a);
    b = findParent(b);
    if (a > b) {
        parent[a] = b;
    } else {
        parent[b] = a;
    }
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    vector<tuple<int, int, int>> nl(m);
    for (int i = 0; i < m; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        nl[i] = {cost, from, to};
    }
    sort(nl.begin(), nl.end());


    int answer = 0;
    for (int i = 0; i < m; i++) {
        int from = get<1>(nl[i]);
        int to = get<2>(nl[i]);
        if (findParent(from) == findParent(to)) { continue; }
        unionParent(from, to);
        answer += get<0>(nl[i]);
    }
    cout << answer;


}
/**
 예제 입력
 7 9
 1 2 29
 1 5 75
 2 3 35
 2 6 34
 3 4 7
 4 6 23
 4 7 13
 5 6 53
 6 7 25
*/