/**
* BaekJoon 1991 트리순회
* programmer: yooj
* Date: 21.08.05
* using: CLion & c++
* Site: https://www.acmicpc.net/problem/1991
**/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
//node 선언
struct node {
    int k;
    node *leftChild;
    node *rightChild;
};
vector<node> tree; // 트리를 저장할 vector

void visited(node *x) { // 방문 처리후 값을 출력
    cout << char(x->k + int('A'));
}

// 전위 순회
void preOrder(node *k) {
    visited(k);
    if (k->leftChild != nullptr) {
        preOrder(k->leftChild);
    }
    if (k->rightChild != nullptr) {
        preOrder(k->rightChild);
    }
}

// 중위 순회
void inOrder(node *k) {
    if (k->leftChild != nullptr) {
        inOrder(k->leftChild);
    }
    visited(k);

    if (k->rightChild != nullptr) {
        inOrder(k->rightChild);
    }
}

// 후위 순회
void postOrder(node *k) {

    if (k->leftChild != nullptr) {
        postOrder(k->leftChild);
    }
    if (k->rightChild != nullptr) {
        postOrder(k->rightChild);
    }
    visited(k);
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    int n;
    cin >> n;
    // tree 에 A = 0, B = 1 과 같이 값을 가지게 트리 생성
    for (int i = 0; i < 26; i++) {
        tree.push_back(node{i, nullptr, nullptr});
    }
    // 트리의 간선을 입력 받음
    for (int i = 0; i < n; i++) {
        char c;
        char left, right;
        cin >> c >> left >> right;
        int parent = c - 'A';
        if (left != '.') {
            tree[parent].leftChild = &tree[left - 'A'];
        }
        if (right != '.') {
            tree[parent].rightChild = &tree[right - 'A'];
        }
    }
    //전위
    preOrder(&tree[0]);
    cout << '\n';
    //중위
    inOrder(&tree[0]);
    cout << '\n';
    //후위
    postOrder(&tree[0]);

}