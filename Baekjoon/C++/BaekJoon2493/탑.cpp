/*
* BaekJoon 2493 탑
* programmer: yooj
* Date: 21.07.26
* using: Pycharm  & Python3
* Site: https://www.acmicpc.net/problem/2493 탑
*/


#include <iostream>
#include <stack>

using namespace std;


stack<pair<int, int>> stk1;  // 기존 배열을 저장하기 위한 스택
stack<pair<int, int>> stk2;  // 비교할 대상을 저작하기 위한 스택
int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;  // 탑의 개수를 저장함
    int ans[n + 1];  // 정답을 저장하기 위한 배열
    fill(ans, ans + n, 0);//0 으로 초기화
    for (int i = 0; i < n; i++) {// 스택에 값을 입력함
        int t;
        cin >> t;
        stk1.push(make_pair(i + 1, t));
    }
    while (!stk1.empty()) {// 스택이 비지 않으면 계속함
        if (stk1.size() == 1)break;// 맨 마지막 탑은 항상 불가능함
        stk2.push(make_pair(stk1.top().first, stk1.top().second));//스택 2에 스택1의 최상단을 push
        stk1.pop();
        while (!stk2.empty() && stk1.top().second > stk2.top().second) {//비교를 해서 해당할경우 답을 추가함
            ans[stk2.top().first] = stk1.top().first;
            stk2.pop();
        }
    }
    for (int i = 1; i < n + 1; i++) {//정답출력
        cout << ans[i] << ' ';
    }
}