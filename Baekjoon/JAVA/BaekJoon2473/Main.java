package boj2473;

import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // input
        int n = Integer.parseInt(br.readLine());
        List<Long> inputNumbers = Arrays.stream(br.readLine().split(" "))
                .map(Long::parseLong)
                .sorted(Long::compareTo)
                .collect(Collectors.toList());
        // 최댓값은 30억 이므로 long 타입으로 저장
        long answer = 3000000003L;

        // 정답을 저장할 배열
        long[] answerNumbers = new long[3];

        // 시작과 끝이 되는 모든 경우를 탐색
        for (int start = 0; start < n; start++) {
            for (int end = start + 2; end < n; end++) {
                int left = start;
                int right = end;
                Long startNumber = inputNumbers.get(start);
                Long endNumber = inputNumbers.get(end);
                // 이분 탐색
                while (left <= right) {
                    int mid = (left + right) / 2;
                    // 서로 다른 세 용액이므로 start 나 end 가 mid 와 같으면 불가능
                    if (mid == start || mid == end) {
                        break;
                    }
                    long tmp = startNumber + inputNumbers.get(mid) + endNumber;
                    long ans = Math.abs(tmp);
                    if (ans < answer) {
                        answer = ans;
                        answerNumbers[0] = startNumber;
                        answerNumbers[1] = inputNumbers.get(mid);
                        answerNumbers[2] = endNumber;
                    }
                    // tmp 에 따라 이분 탐색 방향을 정한다.
                    if (tmp == 0) {
                        break;
                    } else if (tmp < 0) {
                        left = mid + 1;
                    } else if (tmp > 0) {
                        right = mid - 1;
                    }
                }
            }
        }
        // 정답 출력
        for (long answerNumber : answerNumbers) {
            bw.write(Long.toString(answerNumber) + ' ');
        }
        bw.flush();


    }
}
