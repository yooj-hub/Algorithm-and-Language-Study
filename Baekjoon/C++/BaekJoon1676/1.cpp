#include <iostream>

using namespace std;

int main(void) {
//    인풋 아웃풋을 빠르게 하기위한 3줄
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n; //n 을 입력받음
    cin >> n;
    int cnt = 0;
    for (int i = 5; i <= n; i *= 5) { // 팩토리얼의 경우 5의 배수가 2의 배수보다 적으므로 5의 배수의 개수를 셈
        cnt += n / i;
    }
    cout << cnt;

    return 0;

}
