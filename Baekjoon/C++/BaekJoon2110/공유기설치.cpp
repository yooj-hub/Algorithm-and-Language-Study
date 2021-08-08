/**
* BaekJoon 2110 공유기 설치
* programmer: yooj
* Date: 21.08.08
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/2110
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n, c;
    cin >> n >> c;
    vector<int> house(n);
    for (int i = 0; i < n; i++) {
        cin >> house[i];
    }
    sort(house.begin(), house.end());

    int start, end, mid;
    start = 1;//거리의 최솟값
    end = house.back()-house.front(); // 거리의 최댓값
    int val;
    int answer = 0;
    while (start <= end) { // 이분탐색
        mid = (start + end) / 2;
        val = house[0];
        int cnt = 1;
        for (int i = 1; i < n; i++) {
            if (house[i] >= val + mid) {
                val = house[i];
                cnt++;
            }
        }
        if (c <= cnt) {
            answer = mid;
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    cout << answer;

}