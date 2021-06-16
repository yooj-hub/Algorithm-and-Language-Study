/*
 * Baekjoon1260 DFS & BFS
 * programmer: yooj
 * Date: 21.06.15
 * using: IntelliJ & jdk.16.0.1
 * Site: https://www.acmicpc.net/problem/1260
 */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    static boolean[] visited;
    static ArrayList<Integer> slist = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int v = scanner.nextInt();
        visited = new boolean[n + 1];
        int[][] alist = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int l = scanner.nextInt();
            int k = scanner.nextInt();
            alist[l][k] = 1;
            alist[k][l] = 1;
        }
        dfs(n, alist, v);
        for (Integer integer : slist) {
            System.out.print(integer + " ");
        }
        visited = new boolean[n + 1];
        System.out.println();
        bfs(alist, n, v);


    }

    public static void dfs(int n, int[][] alist, int k) {
        visited[k] = true;
        slist.add(k);
        for (int i = 1; i < n + 1; i++) {
            if (alist[k][i] == 1)
                if (!visited[i]) {
                    dfs(n, alist, i);
                }
        }
    }

    public static void bfs(int[][] alist, int n, int k) {
        Deque<Integer> queue = new ArrayDeque<>();
        visited[k] = true;
        queue.add(k);
        while (!queue.isEmpty()) {
            int v;
            v = queue.pop();
            System.out.print(v + " ");
            for (int i = 1; i < n + 1; i++) {
                if (alist[v][i] == 1) {
                    if (!visited[i]) {
                        queue.add(i);
                        visited[i] = true;
                    }
                }
            }

        }
    }


}


