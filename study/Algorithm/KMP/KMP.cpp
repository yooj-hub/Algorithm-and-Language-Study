#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> makeTable(string &pattern) {
    int patternSize = pattern.size();
    vector<int> table(patternSize, 0);
    int j = 0;
    for (int i = 1; i < patternSize; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = table[j - 1];
        }
        if (pattern[i] == pattern[j])
            table[i] += ++j;

    }
    return table;
}

void KMP(string &parent, string &pattern) {
    vector<int> table = makeTable(pattern);
    int parentSize = parent.size();
    int patternSize = pattern.size();
    int j = 0;
    for (int i = 0; i < parentSize; i++) {
        while (j > 0 && parent[i] != pattern[j]) {
            j = table[j - 1];
        }
        if (parent[i] == pattern[j]) {
            if (j == patternSize - 1) {
                cout << i - patternSize + 2 << "번째에서 찾았습니다." << '\n';
                j = table[j];
            } else j++;

        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    string parent = "ababacabacaabacaaba";
    string pattern = "abacaaba";
    KMP(parent,pattern);

}