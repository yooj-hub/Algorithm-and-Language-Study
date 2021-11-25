package boj.boj12852;

import java.io.*;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        // 역순서로 출력하기 위해 계산할 배열
        int[] d = new int[1000001];
        // bfs 에서 중복 탐색을 하지 않기 위해 사용하는 배열
        boolean[] check = new boolean[1000001];

        // 입출력을 위한 BufferedReader and BufferedWriter
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 연산할 n
        int n = Integer.parseInt(br.readLine());

        // BFS 를 하기 위한 Queue
        Queue<Node> q = new ArrayDeque<>();
        // 역 출력을 위한 stk
        Stack<Integer> stk = new Stack<>();
        // BFS 시작을 하기 위한 초기 설정
        q.add(new Node(0, n));
        check[n] = true;
        int answer = -1;
        // BFS
        while (!q.isEmpty()) {
            Node pollNode = q.poll();
            int currentNumber = pollNode.number;
            int currentValue = pollNode.value;
            if (currentValue == 1) {
                answer = currentNumber;
                break;
            }
            // -1 연산
            if (currentValue - 1 > 0 && !check[currentValue - 1]) {
                check[currentValue - 1] = true;
                d[currentValue - 1] = currentValue;
                q.add(new Node(currentNumber + 1, currentValue - 1));
            }
            // /2 연산
            if (currentValue / 2 > 0 && currentValue % 2 == 0 && !check[currentValue / 2]) {
                check[currentValue / 2] = true;
                d[currentValue / 2] = currentValue;
                q.add(new Node(currentNumber + 1, currentValue / 2));
            }
            // /3 연산
            if (currentValue / 3 > 0 && currentValue % 3 == 0 && !check[currentValue / 3]) {
                d[currentValue / 3] = currentValue;
                check[currentValue / 3] = true;
                q.add(new Node(currentNumber + 1, currentValue / 3));
            }

        }
        // 출력
        // 거꾸로 출력하기 위해 스택에 집어 넣음
        int current = 1;
        while (current != 0) {
            stk.add(current);
            current = d[current];
        }
        // 출력
        bw.write(Integer.toString(answer) + '\n');
        while (!stk.empty()) {
            bw.write(Integer.toString(stk.pop()) + ' ');
        }
        bw.write('\n');
        bw.flush();
        bw.close();
        br.close();


    }

    // 큐에 해당 값과 몇번 시도했는지 확인하기 위한 클래스
    private static class Node {
        public int number;
        public int value;

        public Node(int number, int value) {
            this.number = number;
            this.value = value;
        }
    }
}
