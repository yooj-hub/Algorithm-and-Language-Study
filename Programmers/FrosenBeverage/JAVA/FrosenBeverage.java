/*
 * STCT\FrosenBeverage
 * programmer: yooj
 * Date: 21.06.12
 * using: intellij & jdk 16.0.2
 * genre: DFS
 */

import java.util.Scanner;

public class FrosenBeverage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[][] fl = new int[n][m];
        scanner.nextLine();
        for (int j = 0; j < n; j++) {
            String a = scanner.nextLine();
            for (int i = 0; i < m; i++) {
                fl[j][i] = Integer.parseInt(a.substring(i, i + 1));
            }
        }
        int result = 0;
        for(int i = 0;i<n;i++){
            for(int j  = 0; j<m;j++){
                if(dfs(i,j,fl)){
                    result+=1;
                }
            }
        }
        System.out.println(result);


    }

    static boolean dfs(int x, int y, int[][] fl) {
        if (x <= -1 || x >= fl.length || y <= -1 || y >= fl[0].length) {
            return false;
        }
        if (fl[x][y] == 0) {
            fl[x][y] = 1;
            dfs(x - 1, y, fl);
            dfs(x, y - 1, fl);
            dfs(x + 1, y, fl);
            dfs(x, y + 1, fl);
            return true;
        }
        return false;
    }
}
