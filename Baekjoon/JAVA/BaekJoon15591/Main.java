package boj15591;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입출력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // bfs 를 할 그래프
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        // n, q 를 입력받음
        List<Integer> collect = inputData(br);
        int n = collect.get(0);
        int q = collect.get(1);
        int[][] answer = new int[n + 1][n + 1];
        // 그래프 초기화
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }
        // graph init
        for (int i = 0; i < n - 1; i++) {
            List<Integer> input = inputData(br);
            // 방향성이 없게 설정
            graph.get(input.get(0)).add(new Node(input.get(1), input.get(2)));
            graph.get(input.get(1)).add(new Node(input.get(0), input.get(2)));

        }
        // BFS
        for (int i = 1; i < n + 1; i++) {
            Queue<Node> queue = new ArrayDeque<>();
            boolean[] check = new boolean[5001];
            check[i] = true;
            queue.add(new Node(i, 1000000001));
            while (!queue.isEmpty()) {
                Node current = queue.poll();
                for (Node nxt : graph.get(current.getNext())) {
                    if (check[nxt.getNext()]) continue;
                    check[nxt.getNext()] = true;
                    answer[i][nxt.getNext()] = Integer.min(current.getValue(), nxt.getValue());
                    queue.add(new Node(nxt.getNext(), answer[i][nxt.getNext()]));
                }
            }
        }
        // answer 출력
        for (int i = 0; i < q; i++) {
            List<Integer> query = inputData(br);
            // k 보다 큰 경우만 출력 0 번의 경우 0 으로 설정되어 있어 따로 처리할 필요 없다.
            long count = Arrays.stream(answer[query.get(1)]).filter(k -> k >= query.get(0)).count();
            bw.write(count + "\n");
        }
        bw.flush();


    }
    // 입력받을 때 사용한 함수
    private static List<Integer> inputData(BufferedReader br) throws IOException {
        return Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
    }
    // BFS 를 하기 위한 노드
    private static class Node {
        private final int value;
        private final int next;

        public Node(int next, int value) {
            this.value = value;
            this.next = next;
        }

        public int getValue() {
            return value;
        }

        public int getNext() {
            return next;
        }
    }


}
