/**
* BaekJoon 1339 단어수학
* programmer: yooj
* Date: 21.08.10
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/1339
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int alp[26];

int pow(int k) { // 10의 거듭제곱을 구하는 함수
    int res = 1;
    while (k--)res *= 10;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    set<char> set;
    int n;
    cin >> n; // 단어의 개수

    vector<string> sv; // 단어를저장할 벡터
    cin.ignore();
    for (int i = 0; i < n; i++) {
        string str;
        getline(cin, str);
        sv.push_back(str);
        for (char &j : str) { // set 에 알파벳을 등록함
            set.insert(j);
        }
    }
    int l = set.size();
    vector<char> d; // 단어를 벡터에 옮김
    for (char item : set) {
        d.push_back(item);
    }
    int ans = 0;
    //모든 경우에 대하여 연산

    do {
        int tmp = 0;
        int p = 9;
        for (int i = 0; i < l; i++) {
                alp[d[i] - 'A'] = p--;
        }
        for (int i = 0; i < n; i++) {
            int ll = sv[i].size();
            for (int x = 0; x < ll; x++) {
                tmp += alp[sv[i][x] - 'A'] * pow(ll - 1 - x);
            }
        }
        if (tmp > ans) {
            ans = tmp;
        }

    } while (next_permutation(d.begin(), d.end()));
    cout<<ans;


}