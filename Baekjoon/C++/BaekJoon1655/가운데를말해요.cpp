/**
* BaekJoon 1655 가운데를 말해요
* programmer: yooj
* Date: 21.08.14
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/1655
**/

#include <iostream>
#include <queue>


using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    vector<int> numbers;
    int t;
    cin >> t;
    //min heap 과 max heap 선언
    priority_queue<int, vector<int>, greater<>> minHeap;
    priority_queue<int> maxHeap;
    // 처음의 경우 예외 케이스 이므로 미리 처리함
    int tmp;
    cin >> tmp;
    minHeap.push(tmp);
    cout << tmp << '\n';
    int p = 1;
    while (t != p++) {
        cin >> tmp;
        if (minHeap.top() < tmp) // minHeap.top 을 기준으로 처리
            minHeap.push(tmp);
        else {
            maxHeap.push(tmp);
        }
        if (p % 2 == 0) {  // 주어진 수의 개수가 짝수일 경우
            // 두 힙의 사이즈를 같게 만들음
            while (maxHeap.size() < minHeap.size()) {
                maxHeap.push(minHeap.top());
                minHeap.pop();
            }
            while (maxHeap.size() > minHeap.size()) {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
            }
            // 비교하여 답 출력
            if (minHeap.top() > maxHeap.top())
                cout << maxHeap.top() << '\n';
            else {
                cout << minHeap.top() << '\n';
            }
        } else {  // 주어진 수의 개수가 홀수일 경우
            // minHeap 의 크기가 1 더 크게함
            while (maxHeap.size() > minHeap.size()) {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
            }
            cout << minHeap.top() << '\n';

        }

    }
    return 0;
}