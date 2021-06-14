/*
 * STCT
 * programmer: yooj
 * Date: 21.06.12
 * using: intellij & jdk 16.0.2
 */



import java.util.Arrays;
import java.util.Scanner;

public class BiggestNumberRule {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int k = scanner.nextInt();
        int[] nlist= new int[n];
        for(int i = 0; i<n ;i++){
            nlist[i]=scanner.nextInt();
        }
        Arrays.sort(nlist);
        int first = nlist[n-1];
        int second = nlist [n-2];
        int count = 0;
        count+=m/(k+1)*k+m%(k+1);
        System.out.println(count * first + (m-count) * second);

    }

}
