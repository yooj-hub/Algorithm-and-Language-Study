/*
 * Queue Tester
 * programmer: yooj
 * Date: 21.06.22
 * using: IntelliJ & jdk.16.0.1
 */
import java.util.Scanner;

public class QueueTester {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("큐의 크기를 입력하시오");
        int n = scanner.nextInt();
        Queue<Integer> q = new Queue(n);
        boolean on =true;
        while (on) {
            System.out.println("[0] 큐 생성\n" +
                    "[1]큐 add\n" +
                    "[2]큐 pop\n" +
                    "[3]큐 peek\n" +
                    "[4]큐 isEmpty\n" +
                    "[5]큐 isFull\n" +
                    "[6]큐 claer\n" +
                    "[7]큐 size\n" +
                    "[8]큐 indexOf\n" +
                    "[9]종료");
            int menu = scanner.nextInt();

            switch (menu) {
                case 0:
                    System.out.println("[0] 큐 생성");
                    System.out.println("큐의 크기를 입력하시오");
                    int ne = scanner.nextInt();
                    q = new Queue(ne);
                    System.out.println();
                    break;

                case 1:
                    try {
                        System.out.println("[1] 큐 add");
                        System.out.println("삽입할 요소를 입력하시오");
                        int a = scanner.nextInt();
                        q.add(a);
                        System.out.println(a+"이 삽입되었습니다.");
                        System.out.println();
                    }catch(Queue.OverflowEQueueException e){};
                    break;
                case 2:
                    try {
                        System.out.println("[2] 큐 pop");
                        int k = q.pop();
                        System.out.println(k + "가 팝 되었습니다.");
                        System.out.println();
                    }catch(Queue.EmptyEQueueException e){};
                    break;
                case 3:
                    try {
                        System.out.println("[3] 큐 peek");
                        int l = q.peek();
                        System.out.println(l + "가 피크 되었습니다.");
                        System.out.println();

                    }catch(Queue.EmptyEQueueException e){};
                    break;
                case 4:
                    System.out.println("[4] 큐 isEmpty");
                    System.out.println(q.isEmpty());
                    System.out.println();
                    break;
                case 5:
                    System.out.println("[5] 큐 isFull");
                    System.out.println(q.isFull());
                    System.out.println();
                    break;
                case 6:
                    System.out.println("[6] 큐 clear");
                    System.out.println("큐가 지워졌습니다.");
                    System.out.println();
                    q.clean();
                    break;
                case 7:
                    System.out.println("[7] 큐 size");
                    System.out.println("큐의 사이즈는" + q.size() + "입니다");
                    System.out.println();
                    break;
                case 8:
                    System.out.println("[8] 큐 indexOf");
                    System.out.println("찾을 값을 입력하시오");
                    int x = scanner.nextInt();
                    if (x == -1) {
                        System.out.println("존재하지 않습니다.");
                    } else {
                        System.out.println(x+"번째 존재합니다.");
                    }
                    System.out.println();
                    break;
                case 9:
                    System.out.println("종료합니다.");
                    on=false;
                    break;
            }
        }


    }
}
