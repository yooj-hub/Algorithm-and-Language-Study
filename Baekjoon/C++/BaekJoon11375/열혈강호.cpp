#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 1001
using namespace std;

int n, m, ans;
int d[MAX];
bool visited[MAX];
vector<int> a[MAX];

bool dfs(int idx) {
    for (int k : a[idx]) {
        if (visited[k]) continue;
        visited[k] = true;

        if (d[k] == 0 || dfs(d[k])) {
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
    for (int i = 1; i <= n; i++) {
        int queries;
        cin >> queries;
        for (int j = 0; j < queries; j++) {
            int t;
            cin >> t;
            a[i].push_back(t);
        }
    }
    for(int i=1;i<=n;i++){
        fill(visited, visited + MAX, false);
        if (dfs(i)) {
            ans++;
        }
    }
    cout<<ans;

}
