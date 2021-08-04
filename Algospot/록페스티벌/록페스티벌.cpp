#include <iostream>

using namespace std;
int a[1000];//입력을 받을 배열
int d[1000][1001];// 합을 저장하는 배열 ( 앞의 인덱스에서 뒤의 인덱스 까지의 합)

int main() {
    int c;
    scanf("%d", &c); // test case 의 개수를 입력받음
    while (c--) {
        double av = 100.0; // 정답을 저장하는 변수 최댓값이 100이므로 100으로 초기화
        int n, l;
        scanf("%d %d", &n, &l); // n 과 l 을 입력받음
        for (int i = 0; i < n; i++) {
            fill(d[i], d[i] + n + 1, 0); // 0 으로 초기화
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]); // 공연의 비용을 입력 받음
        }
        double com; // 비교하기위한 변수 com

        for (int i = 0; i < n - l + 1; i++) {
            for (int j = i; j < n; j++) {
                if (j == i)
                    d[i][j] = a[j]; // i==j 일 경우 이전 값은 0 이고, i==j==0 일경우 에러가 발생하여 예외처리를 하였다.
                else {
                    d[i][j] = a[j] + d[i][j - 1]; // 모든 수를 더함
                }
                com = (double) d[i][j] / (j - i + 1); // com 은 지금까지 더한 배열을 배열의 개수로 나눈 값임
                if (j - i >= l - 1 && com < av) { // com 이 정답보다 작고, j-i가 l-1 보다 크거나 같을 경우 해당하는 값이므로 av에 저장함
                    av = com;
                }
            }
        }
        printf("%.10lf\n", av); // 정답 출력
    }
    return 0;
}