//StackTester.java

import java.util.Scanner;

public class StackTester {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("스택(인트)의 용량을 입력하시오");
        int n = scanner.nextInt();
        Stack<Integer> stc = new Stack(n);//스택 생성

        while (true) {//스택 push
            try {
                System.out.println("스택에 넣을 값을 입력하시오(종료: q)");
                String str = scanner.next();
                if (str.equals("q")) {
                    System.out.println("Push 종료");
                    break;
                } else {
                    stc.push(Integer.parseInt(str));
                }
            } catch (Stack.OverflowEStackException e) {
                System.out.println("스택이 가득차 삽입되지 않았습니다.");
            }
        }


        while (true) {//스택 pop
            try {
                System.out.println("스택에서 pop 하시겠습니까?(y/n)");
                String str = scanner.next();
                if (str.equals("y")) {
                    System.out.println(stc.pop() + "이 pop 되었습니다.");
                } else {
                    System.out.println("Pop 종료");
                    break;
                }
            } catch (Stack.EmptyEStackException e) {
                System.out.println("스택이 비었습니다");
            }

        }

        while (true) {//스택 indexOf
            try {
                System.out.println("스택에서 찾을 값을 입력하시오 (종료 : q)");
                String str = scanner.next();
                if (str.equals("q")) {
                    System.out.println("IndexOf 종료");
                    break;
                } else {
                    int x = stc.indexOf(Integer.parseInt(str));
                    if (x == -1)
                        System.out.println("존재하지 않습니다.");
                    else
                        System.out.println(x + 1 + "번째 존재합니다.");
                }
            } catch (Throwable e) {
                System.out.println("정수가 아닌 값이 립력되었습니다");
            }

        }


    }
}
