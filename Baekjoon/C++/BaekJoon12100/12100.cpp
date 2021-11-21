#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int n;
int board[20][20];
int gameBoard[20][20];

// 총 5개의 명령어를 만드는 gen
void gen(vector<int> &cmd, int k) {
    for (int j = 0; j < 5; j++) {
        cmd[j] = k & 3;
        k /= 4;
    }
}

// 점수를 구하는 함수
int getScore() {
    int tmp = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (tmp == -1 || tmp < gameBoard[i][j]) {
                tmp = gameBoard[i][j];
            }
        }
    }
    return tmp;
}

void up() {
    bool check[20][20];
    // false 로 초기화
    for (auto &i : check) {
        fill(i, i + 20, false);
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (gameBoard[i][j] == 0) {
                continue;
            }
            int currentRow = i;
            while (true) {
                if (currentRow == 0) break;
                if (check[currentRow - 1][j])
                    break;
                if (gameBoard[currentRow - 1][j]) {
                    if (gameBoard[currentRow][j] == gameBoard[currentRow - 1][j]) {
                        check[currentRow - 1][j] = true;
                        gameBoard[currentRow - 1][j] *= 2;
                        gameBoard[currentRow][j] = 0;
                    }
                    break;
                } else {
                    swap(gameBoard[currentRow][j], gameBoard[currentRow - 1][j]);
                }
                currentRow--;
            }


        }
    }
}

void down() {
    bool check[20][20];
    // false 로 초기화
    for (auto &i : check) {
        fill(i, i + 20, false);
    }

    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j < n; j++) {
            if (gameBoard[i][j] == 0) {
                continue;
            }
            int currentRow = i;
            while (true) {

                if (currentRow == n - 1) {
                    break;
                }
                if (check[currentRow + 1][j])
                    break;
                if (gameBoard[currentRow + 1][j]) {
                    if (gameBoard[currentRow][j] == gameBoard[currentRow + 1][j]) {
                        check[currentRow + 1][j] = true;
                        gameBoard[currentRow + 1][j] *= 2;
                        gameBoard[currentRow][j] = 0;
                    }
                    break;
                } else {
                    swap(gameBoard[currentRow + 1][j], gameBoard[currentRow][j]);
                }
                currentRow++;
            }


        }
    }


}

void left() {
    bool check[20][20];
    // false 로 초기화
    for (auto &i : check) {
        fill(i, i + 20, false);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < n; j++) {
            if (gameBoard[i][j] == 0) {
                continue;
            }
            int currentColumn = j;
            while (true) {
                if (currentColumn == 0)break;

                if (check[i][currentColumn - 1])
                    break;
                if (gameBoard[i][currentColumn - 1]) {
                    if (gameBoard[i][currentColumn - 1] == gameBoard[i][currentColumn]) {
                        check[i][currentColumn - 1] = true;
                        gameBoard[i][currentColumn - 1] *= 2;
                        gameBoard[i][currentColumn] = 0;
                    }
                    break;

                } else {
                    swap(gameBoard[i][currentColumn - 1], gameBoard[i][currentColumn]);
                }
                currentColumn--;

            }

        }
    }


}

void right() {
    bool check[20][20];
    // false 로 초기화
    for (auto &i : check) {
        fill(i, i + 20, false);
    }
    for (int i = 0; i < n; i++) {
        for (int j = n - 2; j >= 0; j--) {
            if (gameBoard[i][j] == 0) {
                continue;
            }
            int currentColumn = j;
            while (true) {

                if (currentColumn == n - 1) {
                    break;
                }
                if (check[i][currentColumn + 1])
                    break;
                if (gameBoard[i][currentColumn + 1]) {
                    if (gameBoard[i][currentColumn + 1] == gameBoard[i][currentColumn]) {
                        check[i][currentColumn + 1] = true;
                        gameBoard[i][currentColumn + 1] *= 2;
                        gameBoard[i][currentColumn] = 0;
                    }
                    break;
                } else {
                    swap(gameBoard[i][currentColumn + 1], gameBoard[i][currentColumn]);
                }
                currentColumn++;
            }

        }
    }


}


// game
void game(vector<int> &cmd, int turn) {
    if (turn == 5)
        return;
    // 상
    if (cmd[turn] == 0) {
        up();
    }
        // 하
    else if (cmd[turn] == 1) {
        down();
    }
        // 좌
    else if (cmd[turn] == 2) {
        left();
    }
        // 우
    else {
        right();

    }
    game(cmd, turn + 1);

}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }
    vector<int> cmd(5);
    int answer = -1;
    for (int i = 0; i < 1024; i++) {
        gen(cmd, i);
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                gameBoard[j][k] = board[j][k];
            }
        }
        game(cmd, 0);
        answer = max(answer, getScore());
    }
    cout << answer;
}