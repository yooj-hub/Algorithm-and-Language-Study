/**
 * SelectionSort.cpp
 * Date: 2021 09 14
 * Programmer: yooj
 * Using: Clion & c++17
 */


#include <algorithm>
#include <vector>

using namespace std;
// int array 를 티용한 정렬
void selectionSort(int *a, const int n) {
    for (int i = 0; i < n; i++) {
        // 제일 처음 수를 기준으루 두고 시작
        int j = i;
        // 최솟값을 찾고 그 인덱스를 j 에 저장한다.
        for (int k = i + 1; k < n; k++) {
            if (a[k] < a[j])
                j = k;
        }
        //두 값을 swap 한다.
        swap(a[i], a[j]);
    }
}

//vector<int> 를 이용한 정렬
void selectionSort(vector<int> &a, const int n) {
    for (int i = 0; i < n; i++) {
        int j = i;
        for (int k = i + 1; k < n; k++) {
            if (a[k] < a[j])
                j = k;
        }
        swap(a[i], a[j]);
    }
}