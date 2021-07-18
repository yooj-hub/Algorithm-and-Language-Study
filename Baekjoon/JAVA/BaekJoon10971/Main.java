/*
 * Baekjoon 10971 외판원 순회 2
 * programmer: yooj
 * Date: 21.07.18
 * using: IntelliJ & JDK 16.0.1
 * Site: https://www.acmicpc.net/problem/10971
 */


import java.io.*;

public class Main {
    static int[][] data; // 각 가는 거리를 저장하기 위한 2차원 배열
    static int ans; // 정답을 구하는데 이용하는 임시 ans
    static boolean[] visited; // 방문한 곳을 확인하는 visited
    static int n; // 총 마을의 개수
    static int answer = Integer.MAX_VALUE; // 정답으로 처음은 int의 제일 큰 수로 설정

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine()); // 마을의 개수를 입력 받음
        data = new int[n][n]; // data 선언
        visited = new boolean[n]; //visited 선언
        ans = 0; // ans 선언
        // data 를 저장하기 위한 for문
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(s[j]);
            }
        }
        visited[0] = true; // 처음 마을을 미리 들린 것으로 처리
        permutation(0, 0); // 정답을 구하기 위한 permutation
        bw.write(Integer.toString(answer)); // 정답 출력
        bw.flush();
    }

    static void permutation(int idx, int start) { // idx 는 들린 마을 수 -1
        if (idx == n - 1) { // 외판원 순회 문제의 경우 시작점이 중요하지 않으므로 처음 시작점을 0으로 잡음
            if (data[start][0] != 0) // 시작점으로 가지 못하는 경우 제외
                if (ans + data[start][0] < answer) { // 최소 거리를 구함
                    answer = ans + data[start][0];
                }
            return;
        }
        // 해당하는 모든 경우의 수를 구하기 위한 for 문
        for (int i = 0; i < n; i++) {
            if (data[start][i] == 0) { // start 에서 i 로 들린다 할 때 가지 못하는 경우 다음으로
                continue;
            }
            if (n - idx > 1 && !visited[i]) { // 총 들린 마을이 n-2 개 일 때까지
                visited[i] = true; // i 번째 마을은 들린 것으로 처리
                ans += data[start][i]; // 비용을 더함
                permutation(idx + 1, i); // 재귀를 통해 다시 연산
                visited[i] = false; // 가지 않은 것으로 처리
                ans -= data[start][i]; // 비용을 원래 값으로 돌림
            }
        }

    }

}
