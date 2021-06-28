
/*
 * Programmers 행렬 테두리 회전하기
 * programmer: yooj
 * Date: 21.06.28
 * using: IntelliJ
 * Site: https://programmers.co.kr/learn/courses/30/lessons/77485
 */
class Solution {
    private int[][] data;
    private int min;

    public int[] solution(int rows, int columns, int[][] queries) {
        int[] ans = new int[queries.length];
        data = new int[rows][columns];
        int pp = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                data[i][j] = pp++;
            }
        }
        min = pp;
        for (int i = 0; i < queries.length; i++) {
            turn(queries[i][0], queries[i][1], queries[i][2], queries[i][3]);
            ans[i] = min;
            min = pp;
        }
        return ans;
    }

    public void turn(int startx, int starty, int endx, int endy) {
        int x = startx - 1;
        int y = starty - 1;
        int ex = endx - 1;
        int ey = endy - 1;
        int start = data[x][y];
        min = start;
        //왼쪽 회전
        for (int i = x; i < ex; i++) {
            int value = data[i + 1][y];
            data[i][y] = value;
            min = Math.min(min, value);
        }
        //아래 회전
        for (int i = y; i < ey; i++) {
            int value = data[ex][i + 1];
            data[ex][i] = value;
            min = Math.min(min, value);
        }
        //오른쪽 회전
        for (int i = ex; i > x; i--) {
            int value = data[i - 1][ey];
            data[i][ey] = value;
            min = Math.min(value, min);
        }
        //위 회전
        for (int i = ey; i > y; i--) {
            int value = data[x][i - 1];
            data[x][i] = value;
            min = Math.min(value, min);
        }
        data[x][y + 1] = start;
    }



}