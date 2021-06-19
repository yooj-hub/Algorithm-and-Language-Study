/*
 * Baekjoon2292
 * programmer: yooj
 * Date: 21.06.19
 * Site: https://www.acmicpc.net/problem/4963
 * using: Intellij & jdk 16.0.1
 */

import java.util.Scanner;

public class Main {
    static boolean[][] visited;//방문 확인을 위하 visited
    static int[][] graph;// 함수에서 전달받지 않고 사용하기위해 전역변수로 graph를 미리선언
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            int n = scanner.nextInt();//가로를 입력받음
            int m = scanner.nextInt();//세로를 입력받음
            if (n == 0 && m == 0) {//n, m 둘다 0 일경우 종료
                break;
            }
            int answer = 0;//정답 초기화
            visited = new boolean[n][m];//매번 시도마다 visited를 가로 , 세로 방향으로 새로만들음
            graph = new int[n][m];//graph도 마찬가지
            //값을 입력받음
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    graph[j][i] = scanner.nextInt();
                }
            }
            //graph중 땅인 부분을 찾음
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (graph[j][i] == 1) {//땅이고
                        if (!visited[j][i]) {//방문하지 않았으면
                            visited[j][i]=true;
                            dfs(j, i, n, m);
                            answer++;
                        }

                    }
                }
            }
            System.out.println(answer);
        }
    }


    public static void dfs(int x, int y, int n, int m) {//dfs함수
        int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1};//x 방향
        int[] dy = {1, 1, 1, 0, -1, -1, -1, 0};//y 방향
        for (int i = 0; i < 8; i++) {//모든 방향에 대해 함수 사용
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < n && ny < m && nx >= 0 && ny >= 0) {//nx, ny가 범위안에 있으면
                if (graph[nx][ny] == 1) {//땅이고
                    if (!visited[nx][ny]) {//들리지 않았으면
                        visited[nx][ny] = true;//해당하는 땅을 true
                        dfs(nx, ny, n, m);//재귀호출
                    }
                }
            }
        }
    }

}