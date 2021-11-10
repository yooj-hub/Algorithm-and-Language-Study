#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> numbers;
int answer = INT32_MAX;
pair<int, int> p;


// 이분탐색을 통한 정답 탐색
void go(int left, int right, int idx) {
    if (left > right) {
        return;
    }
    int mid = (left + right) / 2;
    int tmp = numbers[idx] + numbers[mid];
    // 차이는 무조건 양수로 변경한다.
    int diff = tmp;
    if (tmp < 0) diff = -tmp;
    if (diff < answer) {
        p.first = numbers[idx];
        p.second = numbers[mid];
        answer = diff;
    }
    if (tmp == 0) {
        return;
    }
    if (tmp > 0) {
        go(left, mid - 1, idx);
    } else {
        go(mid + 1, right, idx);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    ///////////////입력///////////////////////////////
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        numbers.push_back(k);
    }
    /////////////////////////////////////////////////

    for (int i = 0; i < n - 1; i++) {
        // 이분탐색의 상한과 하한은 바로 다음것과 마지막 것이다.
        int left = i + 1;
        int right = n - 1;
        go(left, right, i);
    }
    // 정답 출력
    cout << p.first << ' ' << p.second;


}