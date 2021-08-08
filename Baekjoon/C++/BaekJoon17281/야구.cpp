/**
* BaekJoon 17281 야구
* programmer: yooj
* Date: 21.08.08
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/17281
**/
#include <iostream>
#include <algorithm>

using namespace std;

bool visited[9]; //permutation 구현을 위한 Visited
int ans = 0; // 정답을 저장하는 ans
bool base[3]; // 출루 여부를 확인하는 Base
int x[51][9]; // 타자의 안타및 홈런 여부를 저장하는 배열
int out = 0; // 아웃을 저장하는 배열
int inni; // 진행된 이닝수
int score; // 현재 점수
int n; // 총 이닝수
int a[9]; // 순번을 저장하는 배열

void b(int k) { // 출루를 구현한 함수
    if (k == 1) {
        if (base[2]) { // 3루에 있을경우 1점, 3루를 비움
            score++;
            base[2] = false;
        }
        if (base[1]) { // 2루에 있을경우 3루로, 2루를 비움
            base[2] = true;
            base[1] = false;
        }
        if (base[0]) { // 1루에 있을경우 2루로, 1루를 비움
            base[1] = true;
            base[0] = false;

        }
    } else if (k == 2) {
        if (base[2]) { // 3루에 있을경우 1점, 3루를 비움
            score++;
            base[2] = false;
        }
        if (base[1]) { // 2루에 있을경우 1점루 2루를 비움
            base[1] = false;
            score++;
        }
        if (base[0]) { // 1루에 있을경우 3루로, 1루를 비움
            base[2] = true;
            base[0] = false;
        }
    } else if (k == 3) {
        if (base[2]) { // 3루에 있을경우 1점
            score++;
            base[2] = false;
        }
        if (base[1]) { // 2루에 있을경우 1점
            score++;
            base[1] = false;
        }
        if (base[0]) { // 1루에 있을경우 1점
            score++;
            base[0] = false;

        }
    }
}


void baseballGame() {
    while (inni != n) { // 이닝이 n 일 경우 종료
        for (int i : a) {
            int now = x[inni][i]; // 현재 타자의 타석 결과
            if (now == 0) { // 아웃일 경우
                out++;
                if (out == 3) { // 3아웃이면 base 를 모두 비우고 inni 를 1증가시킴
                    out = 0;
                    inni++;
                    fill(base, base + 3, false);
                }
                if (inni == n) {
                    break;
                }
            } else if (now > 0) { // 아웃이 아닌 경우
                if (now == 4) { // 홈런인 경우
                    for (bool &z : base) { // base 를 모두 비우고 base 에 존재하는 타자수 만큼 점수를 더함
                        if (z) {
                            z = false;
                            score++;
                        }
                    }
                    score++;// 타석에 있는 타자의 점수 1 추가
                } else {
                    b(now); // now 만큼 출루 함
                    base[now - 1] = true; // 타석에서 안타를 친 타자를 배치시킴
                }
            }

        }
    }
    if (ans < score) { //ans 의 최댓값을 구함
        ans = score;
    }
    // 이닝 과 점수 초기화
    inni = 0;
    score = 0;

}

//순열을 구하는 알고리즘
void permutations(int idx) {
    if (idx == 9) {
        baseballGame();
        return;
    }
    if(idx==3)
        permutations(idx + 1);
    else {
        for (int i = 1; i < 9; i++) {
            if (!visited[i]) {
                visited[i] = true;
                a[idx] = i;
                permutations(idx + 1);
                visited[i] = false;
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> x[i][j];
        }
    }
    a[3] = 0;//4번타자를 1번타자로 고정

    permutations(0);
    cout << ans;
}
