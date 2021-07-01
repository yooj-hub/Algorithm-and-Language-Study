/*
 * Programmers 등굣길
 * programmer: yooj
 * Date: 21.07.01
 * using: IntelliJ & jdk.16.0.1
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42898
 */


class Solution {
    int mod = 1000000007;//나누기 연산을 위한 mod
    public int solution(int m, int n, int[][] puddles) {
        long[][] d = new long[m][n];//결과를 기록할 d
        boolean[][] visited = new boolean[m][n];//puddles를 기록할 visited
        for (int[] puddle : puddles) {
            visited[puddle[0] - 1][puddle[1] - 1] = true;//puddle이 존재하는 곳을 true로 설정
        }
        d[0][0] = 1;//시작위치 1
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if (i - 1 >= 0) {//i>=1인 경우
                        d[i][j] += d[i - 1][j] % mod;//모듈러의 법칙
                    }
                    if (j - 1 >= 0) {//j>=1인 경우
                        d[i][j] += d[i][j - 1] % mod;//모듈러의 법칙
                    }
                }
            }
        }
        int answer = (int) d[m - 1][n - 1] % mod;//모듈러의 법칙
        return answer;
    }


}