/**
* BaekJoon 1285 동전 뒤집기
* programmer: yooj
* Date: 21.08.29
* using: CLion & c++(17)
* Site: https://www.acmicpc.net/problem/1285
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n;
vector<vector<char>> a(21);

// column을 뒤집는 함수
void changeColumn(vector<vector<char>> &arr, int idx) {
    for (int i = 0; i < n; i++) {
        if (arr[i][idx] == 'T')
            arr[i][idx] = 'H';
        else
            arr[i][idx] = 'T';

    }
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n;
    // 입력을 받음
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (char &j : s) {
            a[i].push_back(j);
        }
    }
    // 초기값을 크게 설정
    int ans = INT32_MAX;
    //비트 마스킹을 이용한 풀이
    for (int i = 0; i < (1 << n); i++) {
        // 배열을 복사해서 연산
        vector<vector<char>> b(a);
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) { // j 번을 선택할 경우 뒤집음
                changeColumn(b, j);
            }
        }
        int cnt = 0;
        // 모든 경우에 대해서 최솟값을 구하면 답
        for (int k = 0; k < n; k++) {
            int tmp = 0;
            for (int l = 0; l < n; l++) {
                if (b[k][l] == 'T')
                    tmp += 1;
            }
            // tmp 가 n-tmp 보다 작을 경우 뒤집은 것으로 처리하여 연산
            if (tmp > n - tmp)
                tmp = n - tmp;
            cnt += tmp;
        }
        ans = min(cnt, ans);
    }
    cout << ans;

}