#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int t;
    cin >> t;
    string cmd;
    int k;
    string numberList;
    cin.ignore();

    while (t--) {
        getline(cin, cmd);
        cin >> k;
        cin.ignore();
        getline(cin, numberList);
        vector<int> numbers;
        int tmp = 0;
        for (int i = 1; i < numberList.length() - 1; i++) {
            if ('0' <= numberList[i] && numberList[i] <= '9') {
                tmp *= 10;
                tmp += numberList[i] - '0';
            } else {
                numbers.push_back(tmp);
                tmp = 0;
            }
        }
        numbers.push_back(tmp);
        int left = 0;
        int right = k;
        bool isReverse = false;
        for (char i : cmd) {
            if (i == 'R') { isReverse = !isReverse; }
            else if(i=='D') {
                if (!isReverse) { left += 1; }
                else { right -= 1; }
            }
        }
        if (left > right) {
            cout << "error" << '\n';
        } else {
            cout << '[';
            if (!isReverse) {
                for (int i = left; i < right; i++) {
                    if (i == right-1) {
                        cout << numbers[i];
                    } else {
                        cout << numbers[i] << ',';
                    }
                }
            } else {
                for(int i = right-1; i>=left ; i--){
                    if(i==left){
                        cout<<numbers[i];
                    }else{
                        cout<<numbers[i]<<',';
                    }
                }
            }
            cout << "]\n";
        }

    }

}