/**
 * BaekJoon 17837 새로운 게임2
 * programmer: yooj
 * Date: 21.08.14
 * using: Intellij & jdk 16.0.2
 * Site: https://www.acmicpc.net/problem/17837
 */

import java.io.*;
import java.util.ArrayList;

public class Main {
    /**
     * dx , dy 움직이는 방향
     * a=turn[a] 시 회전 방향으로 a 변환
     */
    static int[] dx = {0, 0, 0, -1, 1};
    static int[] dy = {0, 1, -1, 0, 0};
    static int[] turn = {0, 2, 1, 4, 3};

    public static void main(String[] args) throws IOException {
        // 입출력 스트림
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //n , k 입력 받음
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);
        int[][] a = new int[n][n];
        for (int i = 0; i < n; i++) {// 체스판을 입력 받음
            s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                a[i][j] = Integer.parseInt(s[j]);
            }
        }
        /**
         * Node 좌표와 방향을 인자로 가짐
         */
        Node[] nl = new Node[k];// 노드 리스트 선언
        //해당 좌표에 있는 말을 표시하기위한 ArrayList<ArrayList<ArrayList<Integer>>> 를 만들고 초기화
        ArrayList<ArrayList<ArrayList<Integer>>> anl = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            anl.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                anl.get(i).add(new ArrayList<>());
            }
        }
        // 좌표에 값을 대입 i 번을 대입함 (1번의 경우 0번으로 처리)
        for (int i = 0; i < k; i++) {
            s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]) - 1;
            int y = Integer.parseInt(s[1]) - 1;
            int direction = Integer.parseInt(s[2]);
            anl.get(x).get(y).add(i);
            nl[i] = new Node(x, y, direction);
        }
        int ans = 0;
        // 답을 구현
        while (ans <= 1000) {
            ans++;
            for (int i = 0; i < k; i++) {
                // i 번째 시작 좌표 및 방향 설정
                    int x = nl[i].x;
                    int y = nl[i].y;
                    int direction = nl[i].direction;
                    int nx = x + dx[direction];
                    int ny = y + dy[direction];
                    // 나가게 될 경우 파란색으로 처리
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        nl[i].direction = turn[direction];
                        direction=turn[direction];
                        nx = x + dx[direction];
                        ny = y + dy[direction];
                        // 반대 방향이 파란색일 경우 스킵
                        if (a[nx][ny] == 2) {
                            continue;
                        }
                    }
                    //파란색 일 경우
                    if (a[nx][ny] == 2) {
                        nl[i].direction = turn[direction];
                        direction=turn[direction];
                        nx = x + dx[direction];
                        ny = y + dy[direction];
                        //반대 방향이 나가게 될 경우 스킵
                        if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                            continue;
                        }
                        // 파란색일 경우 스킵
                        if (a[nx][ny] == 2) {
                            continue;
                        }
                    }
                    //z 는 현재 좌표의 인덱스를 구하고, 그 arrayList 의 크기를 r 에 저장
                    int z = anl.get(x).get(y).indexOf(i);
                    int r = anl.get(x).get(y).size();
                    //빨간색 일 경우 반대로 옮김
                    if (a[nx][ny] == 1) {
                        for (int j = r - 1; j >= z; j--) {
                            int tmp = anl.get(x).get(y).get(j);
                            anl.get(nx).get(ny).add(tmp);
                            nl[tmp].x = nx;
                            nl[tmp].y = ny;
                        }
                    }
                    //투명한 색일 경우 그대로 옮김
                    else if(a[nx][ny]==0) {
                        for (int j = z; j < r; j++) {
                            int tmp = anl.get(x).get(y).get(j);
                            anl.get(nx).get(ny).add(tmp);
                            nl[tmp].x = nx;
                            nl[tmp].y = ny;
                        }
                    }
                    // 옮김 만큼 삭제함
                    if (r > z)
                        anl.get(x).get(y).subList(z, r).clear();
                    // 4이상일 경우 종료이므로 종료조건에 대한 처리를함
                    if (anl.get(nx).get(ny).size() >= 4) {
                        bw.write(Integer.toString(ans) + '\n');
                        bw.flush();
                        System.exit(0);
                    }


            }

        }
        // 1000까지 가서 못 구한 경우 -1 출력
        bw.write("-1\n");
        bw.flush();
    }

// class Node
    static class Node {
        public int x;
        public int y;
        public int direction;

        public Node(int x, int y, int direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
        }

    }

}
