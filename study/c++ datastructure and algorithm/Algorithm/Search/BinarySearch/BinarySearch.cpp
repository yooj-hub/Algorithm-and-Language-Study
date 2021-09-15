/**
 * BinarySearch.cpp
 * Date: 2021 09 15
 * Programmer: yooj
 * Using: Clion & c++17
 */



// x: 찾을 대상 n : 배열의 길이
int binarySearch(int *a, const int x, const int n) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] == x) {
            return mid;
        } else if (a[mid] > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

// bool type 으로 반환
bool binarySearch2(int *a, const int x, const int n) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] == x) {
            return true;
        } else if (a[mid] > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return false;
}

// 재귀를 통한 이진 탐색
bool binarySearchRec(int *a, const int x, const int n, const int left, const int right) {
    int mid = (left + right) / 2;
    if (a[mid] == x) {
        return true;
    } else if (a[mid] > x) {
        return binarySearchRec(a, x, n, left, mid - 1);
    } else {
        return binarySearchRec(a, x, n, mid + 1, right);
    }

}
// 편의를 위한 이진 탐색 함수
bool binarySearchRec(int *a, const int x, const int n) {
    return binarySearchRec(a, x, n, 0, n - 1);
}

// 상한
int upperBound(int *a, const int x, const int n) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] <= x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}

// 하한
int lowerBound(int *a, const int x, const int n) {
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}