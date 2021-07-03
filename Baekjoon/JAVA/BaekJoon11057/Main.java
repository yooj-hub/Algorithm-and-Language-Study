/*
 * BaekJoon 오르막수
 * programmer: yooj
 * Date: 21.07.01
 * using: IntelliJ & jdk.16.0.1
 * Site: https://www.acmicpc.net/problem/11057
 */



import java.util.Scanner;
import java.util.Arrays;
public class Main {
    static int mod = 10007;//나누기 연산을 위한 mod
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] d= new int[n][10];//2차원 배열을 통해 계산
        Arrays.fill(d[0],1);//처음 1자리 일때는 1초 채움
        for(int i=1;i<n;i++){
            for(int j=0;j<10;j++){
                for(int k=0;k<=j;k++){
                    d[i][j]+=d[i-1][k]%mod;
                    d[i][j]%=mod;
                }
            }
        }

        int answer=0;
        for(int i=0;i<10;i++){
            answer+=d[n-1][i]%mod;
            answer%=mod;
        }
        System.out.println(answer);

    }
}
