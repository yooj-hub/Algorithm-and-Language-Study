import java.util.ArrayList;
import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {//main
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        ArrayList<Integer> alit = new ArrayList<>();
        while (true) {//공백 문자 기준으로 토큰을 받음
            int k = str.indexOf(" ");
            if (k == -1) {
                alit.add(Integer.parseInt(str));
                break;
            }
            alit.add(Integer.parseInt(str.substring(0, k)));
            str = str.substring(k + 1);
        }
        System.out.println("Not Sorted : " + alit);
        //////////////Bubble Sort////////////////////////
        /////////////////////////////////////////////////
        int n = alit.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = n - 1; j > i; j--) {
                if (alit.get(j) < alit.get(j - 1)) {
                    int tmp = alit.get(j);
                    alit.set(j, alit.get(j - 1));
                    alit.set(j - 1, tmp);
                }
            }
        }
        ////////////////////////////////////////////////
        System.out.println("Sorted : " + alit);
    }

}

