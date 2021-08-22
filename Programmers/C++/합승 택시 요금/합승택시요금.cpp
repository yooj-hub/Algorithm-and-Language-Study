/**
* Programmers kakao 합승 택시 요금
* programmer: yooj
* Date: 21.08.22
* using: CLion & c++
* Site: https://programmers.co.kr/learn/courses/30/lessons/72413
*/




#include <vector>
#include <algorithm>

#define MX 20000000 // 점이 총 200개 이므로 최대거리를 20만으로 잡음

using namespace std;


// 플로이드 워셜 알고리즘을 이용한 풀이
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = MX;
    int d[201][201];
    for (int i = 0; i < n + 1; i++) {
        fill(d[i], d[i] + n + 1, MX);
    }
    for (int i = 1; i <= n; i++) {
        d[i][i] = 0;
    }
    //양방향 그래프로 설정
    for (const auto &fare : fares) {
        d[fare[0]][fare[1]] = fare[2];
        d[fare[1]][fare[0]]=fare[2];
    }
    //플로이드 워셜 알고리즘
    for (int k = 1; k <= n; k++) {
        for (int j = 1; j <= n; j++) {
            for (int i = 1; i <= n; i++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    int tmp = 0;
    //모든 점에 대하여 거리를 구한다. 만약 경로에 a나 b를 들렸을 경우 그 경우엔 최솟값이 아니기 떄문에 상관없다.
    for (int i = 1; i <= n; i++) {
        tmp = d[s][i] + d[i][a] + d[i][b];
        if (tmp < answer)
            answer = tmp;
    }

    return answer;
}
