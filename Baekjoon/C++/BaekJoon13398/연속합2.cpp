/**
* BaekJoon 13398 연속합 2
* programmer: yooj
* Date: 21.08.16
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/13398
*/

#include <iostream>
#include <algorithm>

using namespace std;

/**
 * d[x][0] -> 숫자를 지우지 않은 X 까지의 최대 연속합
 * d[x][1] -> x-1 번째까지의 숫자중 하나를 지운 x 까지의 최대 연속합
 */

int d[100000][2];

int a[100000]; // 입력값을 저장할 배열


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    // answer 의 첫값을 a[0] 으로 설정
    int answer = a[0];
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            //첫 값은 전 값이 없으므로 a[0]이 최대인 연속합
            d[i][0] = a[0];
            continue;
        } else if (i == 1) {
            // 1일 경우
            if (d[i - 1][0] < 0) {
                d[i][0] = a[i];
            } else {
                d[i][0] = a[i] + d[i - 1][0];
            }
            // 처음 값을 제외한 값이 숫자 하나를 지운 최대 연속합
            d[i][1] = a[i];
        } else {
            if (d[i - 1][0] < 0) {
                // 전의 d의 값이 0 이하면 a[i] 가 가장큰 연속합니다.
                d[i][0] = a[i];

            } else {
                // 그 외엔 더한 값이 제일 큰 연속합
                d[i][0] = a[i] + d[i - 1][0];
            }
            // 1개를 건너 띈 연속합의 최댓값은 i-2 번째를 건넌 값 또는, 기존의 1개를 건넌 i-1 번째 연속합에 a[i]를 더한 값이다.
            d[i][1] = max(d[i - 1][1], d[i - 2][0]) + a[i];
        }
        //최댓값 구하기
        if (answer < d[i][0]) {
            answer = d[i][0];
        }
        if (answer < d[i][1]) {
            answer = d[i][1];
        }
    }
    //정답출력
    cout << answer;


}