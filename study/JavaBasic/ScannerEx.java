//ScannerEx.java

import java.util.InputMismatchException;//Exception Handling
import java.util.Scanner;//Scanner 객체 사용

public class ScannerEx {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("1) scanner.next()");//다음 토큰을 1개 입력받음
        String a1 = scanner.next();//String으로 입력을 받음
        System.out.println("1) " + a1);
        System.out.println();
        scanner.nextLine();//전에 있는 개행문자 제거

        while (true) {//8비트 확인을 위한 반복문
            try {
                System.out.println("2) scanner.nextByte()");
                byte a2 = scanner.nextByte();//Byte형은 8 비트의 정수를 입력 받음(-128 ~ 127)
                System.out.println("2) " + a2);
                System.out.println();
                break;
            } catch (InputMismatchException e) {
                e.printStackTrace();
                scanner.nextLine();
            }
        }

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("3) scanner.nextShort()");
        short a3 = scanner.nextShort();//short형은 16비트의 정수를 입력받음(-32768 ~ 32767)
        System.out.println("3) " + a3);
        System.out.println();

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("4) scanner.nextInt()");
        int a4 = scanner.nextInt();//int형은 32비트의 정수를 입력받음(-21억 ~ 21억)
        System.out.println("4) " + a4);
        System.out.println();

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("5) scanner.nextLong()");
        long a5 = scanner.nextLong();//long형은 64비트의 정수를 입력받음(-2^63 ~ 2^63-1)
        System.out.println("5) " + a5);
        System.out.println();

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("6) scanner.nextFloat()");
        float a6 = scanner.nextFloat();//32비트의 실수를 입력받음
        System.out.println("6) " + a6);
        System.out.println();

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("7) scanner.nextDouble()");
        double a7 = scanner.nextDouble();
        System.out.println("7) " + a7);//64비트의 실수를 입력받음
        System.out.println();

        scanner.nextLine();//전에 있는 개행문자 제거
        System.out.println("8) scanner.nextBoolean()");
        boolean a8 = scanner.nextBoolean();
        System.out.println("8) " + a8);//boolean형 변수를 입력받음(true or false)
        System.out.println();

        System.out.println("9) scanner.nextLine");
        scanner.nextLine();//전에 있는 개행문자 제거
        String a9 = scanner.nextLine();//1줄 전체를 입력받음 개행문자를 통해 나눠짐
        System.out.println("9) " + a9);
        System.out.println();

        scanner.close();//스캐너 종료

    }
}
