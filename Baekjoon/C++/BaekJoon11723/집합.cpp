/*
* BaekJoon 11723 집합
* programmer: yooj
* Date: 21.07.24
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/11723
*/


#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    //cout, cin 을 아용하기 윈한 처리
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    //총 개수를 입력 받음
    int m;
    cin >> m;
    int k = 1;
    string cmd;// 명령어를 입력받을 cmd
    int n; // cmd 에 수가 필요한 경우 입력 받음
    while (m--) {
        cin >> cmd; // 명령어를 입력 받음
        if (cmd == "all" || cmd == "empty");// add 나 all 일경우 다음 수가 필요 없음
        else {
            cin >> n;
        }
        if (cmd == "add") {// add 일 경우 or 연산자를 이용하여 연산
            k |= (1 << n);
        } else if (cmd == "check") { // check 일경우 & 연산자를 통해 확인
            if ((k & (1 << n)) != 0) {
                cout << 1 << '\n';
            } else {
                cout << 0 << '\n';
            }
        } else if (cmd == "remove") { //remove 일경우 & 와 ~ 을 이용하여 연산
            k &= ~(1 << n);

        } else if (cmd == "toggle") { // toggle 일경우 ^ 연산자를 이용하여 연산
            k ^= (1 << n);

        } else if (cmd == "all") { // all 일 경우 2 ~ 2^20 승의 합으로 바꿔줌
            k = (1 << 21) - 2;

        } else {
            k = 1; // empty 인경우 1로 돌림
        }


    }
}