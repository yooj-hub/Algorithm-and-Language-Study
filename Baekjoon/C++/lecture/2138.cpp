#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n;
vector<int> numbers[2];

void push(int idx) {
    if (idx == 0) {
        numbers[0][idx] = numbers[0][idx] == 0 ? 1 : 0;
        numbers[0][idx + 1] = numbers[0][idx + 1] == 0 ? 1 : 0;


    } else if (idx == n - 1) {
        numbers[0][idx - 1] = numbers[0][idx - 1] == 0 ? 1 : 0;
        numbers[0][idx] = numbers[0][idx] == 0 ? 1 : 0;
    } else {
        numbers[0][idx - 1] = numbers[0][idx - 1] == 0 ? 1 : 0;
        numbers[0][idx] = numbers[0][idx] == 0 ? 1 : 0;
        numbers[0][idx + 1] = numbers[0][idx + 1] == 0 ? 1 : 0;
    }
}

int go(int idx, int value) {
    if (idx == n) {
        for (int i = 0; i < n; i++) {
            if (numbers[0][i] == numbers[1][i])
                continue;
            else {
                return -1;
            }
        }
        return value;
    }
    if (idx == 0) {
        push(idx);
        int tmp = go(idx + 1, value + 1);
        push(idx);
        int tmp2 = go(idx + 1, value);
        if (tmp == tmp2)return tmp;
        if (tmp == -1) return tmp2;
        if (tmp2 == -1) return tmp;
        if (tmp < tmp2) return tmp;
        if (tmp > tmp2) return tmp2;
    } else {
        if (numbers[0][idx - 1] == numbers[1][idx - 1])
            return go(idx + 1, value);
        else {
            push(idx);
            int tmp = go(idx + 1, value + 1);
            push(idx);
            return tmp;
        }
    }

}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);

    cin >> n;
    for (auto &number : numbers) {
        string str;
        cin >> str;
        for (const auto &item : str) {
            number.push_back(item - '0');
        }
    }
    cout<< go(0,0);


}