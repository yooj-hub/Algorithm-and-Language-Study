#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> a[101];
int d[101];
bool visited[101];
int n;
int ans;

bool note(int idx) {
    for (int k : a[idx]) {
        if (visited[k])
            continue;
        visited[k] = true;
        if (d[k] == 0 || note(d[k])) {
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
    int m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int f, t;
        cin >> f >> t;
        a[f].push_back(t);
    }
    for(int i=1;i<n+1;i++){
        fill(visited + 1, visited + 100, false);
        if(note(i))ans++;
    }
    cout << ans;
}