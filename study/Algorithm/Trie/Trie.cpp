struct Trie {
    struct Node {
        int children[26]; // 소문자만 추가
        bool valid;

        Node() {
            for (int &i : children) {
                i = -1;
            }
            valid = false;// true 추가한, false 중간
        }
    };

    vector<Node> trie;
    int root;

    int init() {
        Node x;
        trie.push_back(x);
        return (int) trie.size() - 1; // 추가한 노드의 idx 리턴
    }

    Trie() {
        root = init();
    }

    // node 탐색하고 있는 노드의 인덱스 s 추가하려고 하는 문자열 s 의 인덱스를 추가하고 있는가
    void add(int node, string &s, int index) {
        if (index == s.size()) {
            trie[node].valid = true;
            return;
        }
        int c = s[index] - 'a';
        if (trie[node].children[c] == -1) {
            int next = init();
            trie[node].children[c] = next;
        }
        int child = trie[node].children[c];
        add(child, s, index + 1);

    }

    bool search(int node, string &s, int index) {
        if (node == -1)return false;
        if (index == s.length())return trie[node].valid;
        int c = s[index] - 'a';
        int child = trie[node].children[c];
        return search(child, s, index + 1);
    }
};