import java.io.*;

public class Main2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine()); // 마을의 개수를 입력 받음
        int[][] data = new int[n][n]; // data 선언
        int answer = Integer.MAX_VALUE; // 처음 정답은 인트의 최댓값으로 설정함
        // data 입력
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(s[j]);
            }
        }
        int[] d = new int[n]; // 목적지를 적는 d 함수 선언
        for (int i = 0; i < n; i++) {  // 처음 목적지를 제일 작은 순열로 입력함
            d[i] = i;
        }
        do {
            if(d[0]!=0) // 시작점을 고정
                break;
            int ans = 0; // 처음값 0
            boolean check = true; // 갈 수 없는 곳을 들리는지 확인하기 위한 boolean 변수
            for (int i = 0; i < n - 1; i++) {
                if (data[d[i]][d[i + 1]] == 0) { // 갈 수 없으면
                    check = false;
                    break;
                } else {
                    ans += data[d[i]][d[i + 1]]; //
                }
            }
            if (check && data[d[n - 1]][d[0]] != 0) { // 갈 수 없는 곳을 들리지 않았고, 0 으로 갈 수 있으면
                ans += data[d[n - 1]][d[0]];
                answer = Math.min(ans, answer); // 정답 추출
            }

        } while (nextPermutation(d)); // 다음 순열이 있으면 구함
        bw.write(Integer.toString(answer)); // 문제에서 무조건 이어지는 길이 있다했으니 정답 추출
        bw.flush();


    }

    static boolean nextPermutation(int[] a) { // 다음 순열을 구하기 위한 함수
        int i = a.length-1;
        while (i > 0 && a[i - 1] > a[i]) {
            i--;
        }
        if (i <= 0) {
            return false;
        }
        int j = a.length - 1;
        while (a[i - 1] >= a[j]) {
            j--;
        }
        swap(a, i - 1, j);
        j = a.length - 1;
        while (i < j) {
            swap(a, i, j);
            i++;
            j--;
        }
        return true;
    }

    static void swap(int[] arr, int idx1, int idx2) { // 서로 바꿔주는 함수
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

}
