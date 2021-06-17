//RandomEx.java
import java.util.Random;//Random 클래스 생성을위한 import

public class RandomEx {
    public static void main(String[] args) {
        Random generator = new Random();//난수 생성을 위한 Random 객체 선언
        int a1 = generator.nextInt();//1) 변수가 없을시 -2^31 ~ 2^31-1 리턴
        System.out.println("1) nextInt()");
        System.out.println("1) " + a1);//Byte short long도 지원함
        System.out.println();

        System.out.println("2) nextInt(10)");
        int a2 = generator.nextInt(10);//2) 0에서 괄호안의 숫자미만의 리턴
        System.out.println("2)" + a2);
        System.out.println();

        System.out.println("3) nextFloat()");
        float a3 = generator.nextFloat();//0이상 1미만의 임의의 float 리턴
        System.out.println("3)" + a3);
        System.out.println();

        System.out.println("4) nextDouble()");
        double a4 = generator.nextDouble();//0이상 1미만의 임의의 double 리턴
        System.out.println("4)" + a4);
        System.out.println();

        System.out.println("5) Math.random()");
        double a5 = Math.random();//Math.Random은 0이상 1미만의 임의의 double 리턴
        System.out.println("5)" + a5);
        System.out.println();

        System.out.println("Ex) 100 ~ 199 나타내기");
        System.out.println("nextInt(100)+100");
        System.out.println(generator.nextInt(100) + 100);


    }
}
