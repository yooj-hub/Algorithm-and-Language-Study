/*
 * Baekjoon1439 문자열 뒤집기
 * programmer: yooj
 * Date: 21.06.18
 * using: IntelliJ & jdk.16.0.1
 * Site: https://www.acmicpc.net/problem/1439
 */

import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String str=scanner.nextLine();
        int n = str.length();
        int answer=0;
        for(int i=1;i<n;i++){
            if(str.charAt(i-1)!=str.charAt(i)){//전과 다를 경우 answer++
                answer++;
            }
        }
        if(str.charAt(0)==str.charAt(n-1))//처음과 끝이 같으면 answer/2 출력
            System.out.println((answer/2));
        else{
            System.out.println((answer/2)+1);//처음과 끝이 다르면 answer/2+1출력

        }

    }
}
