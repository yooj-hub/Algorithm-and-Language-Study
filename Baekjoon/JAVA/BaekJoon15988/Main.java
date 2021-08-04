/**
 * BaekJoon 15988 1,2,3 더하기 3
 * programmer: yooj
 * Date: 21.08.04
 * using: Intellij & jdk 16.0.2
 * Site: https://www.acmicpc.net/problem/15988
 */

import java.io.*;

public class Main {
    static int mod = 1000000009; // 나누기 연산을 위한 mod

    public static void main(String[] args) throws IOException {
        long[] d = new long[1000001];// memorization 을 하기 위한 배열
        //입출력 스트림
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());// test case 개수
        int p = -1;
        while (t != 0) {
            t--;
            int n = Integer.parseInt(br.readLine());
            for (int i = p+1; i <= n; i++) { // p 부터 n 까지 시행함
                if (i == 0) {
                    d[i] = 1;
                } else if (i == 1) {
                    d[i] = d[i - 1];
                } else if (i == 2) {
                    d[i] = d[i - 1] + d[i - 2];
                } else {
                    d[i] = d[i - 1] + d[i - 2] + d[i - 3];
                    d[i] %= mod;
                }
            }
            bw.write(Long.toString(d[n]) + '\n');
            bw.flush();
            if (p == -1 || p < n) {// p < n 일 경우 p 를 n 으로 바꾸고 다시 하게됨
                p = n;
            }
        }
    }
}
