/*
 * Baekjoon 설탕배달
 * programmer: yooj
 * Date: 21.06.26
 * using: IntelliJ
 * Site: https://www.acmicpc.net/problem/2839
 */


import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();//.n을 입력받음
        int answer=0;
        while (n>=1){
            if((n%5)==0) {//5로 나눠지면 5로 나누고 5로나눈 몫을 answer에 더하고 종료
                answer += n / 5;
                n=0;
            }
            else{//5로 안나눠질 경우 3을 뺴고 answer+1
                n=n-3;
                answer+=1;
            }
        }
        if(n==0){//n=0일 경우 answer 출력
            System.out.println(answer);
        }
        else//아닐경우 -1
            System.out.println(-1);
    }
}
