/**
* BaekJoon 10942 팰린드롬?
* programmer: yooj
* Date: 21.08.12
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/10942
**/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> numbers;  // 수열을 저장할 벡터
bool check[2001][2001]; // 결과를 저장할 배열

// 팰린드롬인지 체크하는 함수
void checkF(int start, int end) {
    if (start == end) { // 시작과 끝이 같으면 항상 팰린드롬임
        check[start][end] = true;
        return;
    }
    if (numbers[start] == numbers[end]) {  // 시작과 끝의 수가 같고
        if (end - start == 1) { // 서로 연속되는 수면 무조건 팰린드롬
            check[start][end] = true;
            return;
        } else if (check[start + 1][end - 1]) { // 안의 수열이 팰린드롬이면 팰린드롬
            check[start][end] = true;
            return;
        } else { // 팰린드롬이 아닐경우 아님
            check[start][end] = false;
            return;
        }
    }
    check[start][end] = false;  // 시작과 끝의 수가 다르면 팰린드롬이 아니다.
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    numbers.push_back(0);
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        numbers.push_back(tmp);
    }
    for (int i = n; i > 0; i--) { // 끝에서 부터 연산
        for (int j = i; j < n + 1; j++) {
            checkF(i, j);
        }
    }
    int m;
    cin >> m;
    while (m--) { // 정답 출력
        int f, t;
        cin >> f >> t;
        cout << check[f][t] << '\n';
    }

}
