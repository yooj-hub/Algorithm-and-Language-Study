/**
* BaekJoon 1753 최단경로
* programmer: yooj
* Date: 21.08.21
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/1753
*/


#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
#define INF 123456789

using namespace std;
vector<pair<int, int>> vertex[20001];
int d[20001];


void dijkstra(int start) { // 다익스트라 알고리즘
    d[start] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, start});
    while (!pq.empty()) {
        int dist = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        for (auto c : vertex[cur]) {
            int cost = dist + c.first;
            if (cost < d[c.second]) {
                d[c.second] = cost;
                pq.push({cost, c.second});
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int v, e;
    cin >> v >> e;
    fill(d, d + v + 1, INF); // 모든 정점에 대한 거리를 INF로 채움
    int start;
    cin >> start;
    for (int i = 0; i < e; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        vertex[from].emplace_back(cost, to);// pair 자료형을 이용하여 간선리스트 작성을 통해 구현
    }
    dijkstra(start);
    for (int i = 1; i <= v; i++) {
        if (d[i] == INF) // 도달 못할경우 INF 출력
            cout << "INF" << '\n';
        else
            cout << d[i] << '\n';
    }

}