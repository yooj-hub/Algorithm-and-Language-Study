#include <iostream>
#include <vector>
#include <algorithm>
#include<queue>
#include <unordered_set>

using namespace std;
int n;
int W[16][16];

struct node {
    int bound;
    int level;
    unordered_set<int> path;


};

int length(node &u) {
    vector<int> path;
    for (const auto &item : u.path) {
        path.push_back(item);
    }
    int res = 0;
    for (int i = 1; i < path.size(); i++) {
        res += W[path[i - 1]][path[i]];
    }
    res += W[path[path.size() - 1]][0];
    return res;
}


int pow(int x) {
    if (x <= 0) {
        return 1;
    }
    if (x == 1) {
        return 2;
    }
    if (x % 1) {
        int tmp = pow(x / 2);
        return tmp * tmp * 2;
    } else {
        return 2 * pow(x - 1);
    }
}

int bound(node &v) {
    vector<int> A;
    vector<int> p;
    int bound = 0;
    int b = 0;
    for (const auto &path : v.path) {
        p.push_back(path);
        b += pow(path);

    }
    for (int i = 0; i < n; i++) {
        if (b & pow(i)) continue;
        A.push_back(i);

    }
    for (int i = 1; i < p.size(); i++) {
        bound += W[p[i - 1]][p[i]];
    }

    int k = p[p.size() - 1];
    int m = INT32_MAX;
    for (int i : A) {
        m = min(m, W[k][i]);
    }
    bound += m;
    for (int i = 0; i < A.size(); i++) {
        int pv = i;
        int tmpm = W[i][0];
        for (int j = 0; j < A.size(); j++) {
            if (j == pv) continue;
            tmpm = min(tmpm, A[j]);

        }
        bound += tmpm;
    }


    return bound;

}


void travel(unordered_set<int> &optTour, int &minLength) {
    queue<node> q;
    node u, v;
    v.level = 0;
    v.path.insert(0);
    v.bound = bound(v);
    minLength = INT32_MAX;
    q.push(v);
    while (!q.empty()) {
        v = q.front();
//        for (const auto &path : v.path) {
//            cout<<path << ' ';
//        }
//        cout << '\n';
        q.pop();
        if (v.bound < minLength) {
            u.level = v.level + 1;
            for (int i = 1; i < n; i++) {
                if (v.path.find(i) == v.path.end()) {

                    for (const auto &path : v.path) {
                        cout<<path<<' ';
                        u.path.insert(path);
                    }
                    cout<<'\n';
                    u.path.insert(i);
                    for (const auto &path : u.path) {
                        cout<<path << ' ';
                    }

                    cout << "\n------------------end----------\n";
                    if (u.level == n - 2) {
                        for (int k = 0; k < n; k++) {
                            if (u.path.find(k) == u.path.end()) {
                                u.path.insert(k);
                                if (length(u) < minLength) {
                                    minLength = length(u);
                                    optTour = u.path;
                                }
//                                u.path.erase(k);
                            }
                        }


                    } else {
                        u.bound = bound(u);
                        if (u.bound < minLength) q.push(u);
                    }
                }
            }
        }
    }


}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
//    cout<<pow(10);

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> W[i][j];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(W[i][j] == 0){
                W[i][j] = 9876543210;
            }
        }
    }
    unordered_set<int> optTour;
    int answer = INT32_MAX;
    travel(optTour, answer);
    cout << answer;
    cout << '\n';
    for (const auto &item : optTour) {
        cout<<item<<'\n'
    ;}


}