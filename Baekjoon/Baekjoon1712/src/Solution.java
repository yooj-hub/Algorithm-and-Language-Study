/*
 * Baekjoon1712
 * programmer: yooj
 * Date: 21.06.11
 */

import java.util.Scanner;
public class Solution {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int A=scanner.nextInt();
        int B=scanner.nextInt();
        int C=scanner.nextInt();
        if(B>C||C==0)
            System.out.print(-1);
        else {
            int div = C-B;
            int answer = A/div;
            answer++;


            System.out.print(answer);
        }



    }
}
