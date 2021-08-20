#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<pair<int, int>> vertex[100];
int d[100];

void dijkstra(int start) {
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
    fill(d, d + v, 1234567890);
    int start;
    cin >> start;
    for (int i = 0; i < e; i++) {
        int from, to, cost;
        cin >> from >> to >> cost;
        vertex[from].emplace_back(cost, to);
    }
    dijkstra(start);
    for(int i=1;i<=v;i++){
        cout<<d[i]<<endl;
    }

}