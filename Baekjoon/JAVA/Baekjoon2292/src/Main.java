/*
 * Baekjoon2292
 * programmer: yooj
 * Date: 21.06.11
 */

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int right=2;
        int pv=1;
        if(N==1)
            System.out.println(1);
        else {
            while (true) {
                if (right > N)
                    break;
                right += pv * 6;
                pv++;
            }
            System.out.println(pv);
        }

    }
}
