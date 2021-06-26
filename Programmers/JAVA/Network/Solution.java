/*
 * Programmers 네트워크
 * programmer: yooj
 * Date: 21.06.26
 * using: IntelliJ
 * Site: https://programmers.co.kr/learn/courses/30/lessons/43162
 */
import java.util.HashSet;//개수 세기를 위한 hashset

class Solution {
    static int[] parent;

    public int solution(int n, int[][] computers) {
        HashSet<Integer> set = new HashSet<>();
        parent = new int[n];
        for (int i = 0; i < n; i++) {//자기 자신의 부모를 자기자신으로 설정
            parent[i] = i;
        }
        for (int i = 0; i < n; i++) {
            connectNode(computers, i);//노드 연결
        }
        for (int i = 0; i < n; i++) {
            set.add(findParent(parent, parent[i]));//hash셋을 이용하여 개수를셈
        }
        return set.size();
    }

    public int findParent(int[] parent, int x) {//부모 찾기
        if (x == parent[x])
            return x;
        return parent[x] = findParent(parent, parent[x]);
    }

    public void unionParent(int a, int b) {//부모 결합
        a = findParent(parent, a);
        b = findParent(parent, b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public void connectNode(int[][] computers, int k) {//노드 연결
        for (int i = k + 1; i < computers.length; i++) {
            if (computers[k][i] == 1) {
                unionParent(k, i);

            }
        }
    }

}