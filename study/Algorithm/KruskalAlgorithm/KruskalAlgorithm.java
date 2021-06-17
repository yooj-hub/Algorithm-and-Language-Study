/* KruskalAlgorithm.java
 * Programmers KruskalAlgorithm
 * programmer: yooj
 * Date: 21.06.17
 * using: intellij & jdk 16.0.1
 * site: https://github.com/ndb796
 */
import java.util.Scanner;
import java.util.Arrays;

public class KruskalAlgorithm {
    public static int findParent(int[] parents, int x) {//루트를 찾는 메소드
        if (parents[x] != x) {//루트가 자시자신이 아니면
            parents[x] = findParent(parents, parents[x]);//parent[x]를 기준으로 parents[x]를 정의
        }
        return parents[x];//루트노드를 리턴
    }

    public static void unionParent(int[] parents, int a, int b) {
        a = findParent(parents, a);
        b = findParent(parents, b);
        if (a < b)//작은 쪽이 부모
            parents[b] = a;
        else
            parents[a] = b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int v = scanner.nextInt();//vertex
        int e = scanner.nextInt();//edge
        int[] parents = new int[v + 1];//0을 사용하지않기 떄문에 vertex+1로 초기화
        Edges[] edges = new Edges[e];//Edges 클래스 (cost, start, end)
        int result = 0;//결과값
        for (int i = 1; i < v + 1; i++) {//부모를 자기자신이 가르키게 설정
            parents[i] = i;
        }
        for (int i = 0; i < e; i++) {//Edges를 통해 edges 정의
            edges[i] = new Edges(scanner.nextInt(), scanner.nextInt(), scanner.nextInt());
        }
        Arrays.sort(edges);//오름차순 정렬
        //KruskalAlgorithm
        for (int i = 0; i < e; i++) {
            if (findParent(parents, edges[i].start) != findParent(parents, edges[i].end)) {//cycle이 아니면
                unionParent(parents, edges[i].start, edges[i].end);//두 노드를 연결
                result += edges[i].cost;// 그 만큼 cost 증가
            }
        }
        System.out.println(result);//cost 출력


    }

    public static class Edges implements Comparable<Edges> {//Edges class
        public int cost;
        public int start;
        public int end;

        Edges(int start, int end, int cost) {//Constructor
            this.start = start;
            this.end = end;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edges o) {//Comparable
            return this.cost > o.cost ? 1 : -1;
        }
    }
}
