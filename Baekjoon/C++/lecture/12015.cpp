#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        auto it = lower_bound(a.begin(), a.end(), num);
        if(it == a.end()){
            a.push_back(num);
        }else{
            *it = num;
        }
    }
    cout << a.size();
}