#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int parent[100];


int findDirectParent(int x) {
    if (parent[x] == x)return x;
    return findDirectParent(parent[x]);
}

int findParent(int x) {
    if (parent[x] == x)return parent[x];
    return findParent(parent[x]);
}

bool unionParent(int a, int b) {
    bool cycle = false;
    a = findParent(a);
    b = findParent(b);
    if (a == b) cycle = true;
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
    return cycle;
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    for(int i=1;i<=6;i++){
        parent[i]=i;
    }
    unionParent(1,4);
    unionParent(2,3);
    unionParent(2,4);
    unionParent(5,6);
    for (const auto &item : parent) {
        if(item!=0){
            cout<<item<<endl;
        }

    }

}