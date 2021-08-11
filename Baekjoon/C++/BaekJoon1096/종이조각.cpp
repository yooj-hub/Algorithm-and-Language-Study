#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int pow(int k) {
    int res = 1;
    while (k--)
        res *= 10;
    return res;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> a[n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int k;
            scanf("%1d", &k);
            a[i].push_back(k);
        }
    }
    int ans = 0;
    for (int i = 0; i <= (1 << (n * m)) - 1; i++) {
        int tmp = 0;
        for (int j = 0; j < n; j++) {
            int cnt = 0;
            int k = 0;
            for (; k < m; k++) {
                if ((1 << (j * m + k)) & i) {
                    cnt++;
                } else {
                    for (int x = 0; x < cnt; x++) {
                        tmp += a[j][k - x - 1] * pow(x);

                    }
                    cnt = 0;

                }

            }
            for (int x = 0; x < cnt; x++) {
                tmp += a[j][k - x - 1] * pow(x);
            }
        }
        for (int j = 0; j < m; j++) {
            int cnt = 0;
            int k = 0;
            for (; k < n; k++) {
                if (((1 << (j + k * m)) & i) == 0) {
                    cnt++;
                } else {
                    for (int x = 0; x < cnt; x++) {
                        tmp += a[k - x - 1][j] * pow(x);
                    }
                    cnt = 0;
                }
            }
            for (int x = 0; x < cnt; x++) {
                tmp += a[k - x - 1][j] * pow(x);

            }

        }
        if (tmp > ans)
            ans = tmp;
    }

    printf("%d", ans);
    return 0;


}