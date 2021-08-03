/**
* BaekJoon 5557 1학년
* programmer: yooj
* Date: 21.08.03
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/5557
**/

#include <iostream>

using namespace std;
int n;
int a[99];

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n - 1; i++) { // 마지막 수를 제외하고 입력을 받음
        cin >> a[i];
    }
    int target; // 마지막 수를 target 에 저장
    cin >> target;
    long long d[n - 1][21]; // 다이나믹 프로그래밍을 위한 배열
    for (auto &i : d) { // 전부 0으로 채움
        fill(i, i + 21, 0);
    }
    /**
     * d[a][b] 의 의미는 지금까지의 계산결과가 b 이며, a 번째 수를 계산한 결과 이다.
     */
    for (int i = 0; i < n - 1; i++) {
        if (i == 0) {
            d[i][a[i]] = 1; // i == 0 일 경우 다른 수와 비교할 필요 없이 d[i][a[i]] 에 저장
        } else {
            for (int j = 0; j < 21; j++) {
                if (d[i - 1][j] != 0) {
                    if (j + a[i] >= 0 && j + a[i] <= 20) { // 더하는 경우
                        d[i][j + a[i]] += d[i - 1][j];
                    }
                    if (j - a[i] >= 0 && j - a[i] <= 20) { // 빼는 경우
                        d[i][j - a[i]] += d[i - 1][j];
                    }
                }
            }
        }
    }
    cout << d[n - 2][target];
}