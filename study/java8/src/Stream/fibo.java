package Stream;

import java.util.Arrays;
import java.util.stream.Collector;
import java.util.stream.Stream;

public class fibo {

    public static void main(String[] args) {
        System.out.println("fibon(10) = " + fibon(10));

    }

    public static int fibon(int n) {
        return Stream.iterate(new int[]{0,1}, t -> new int[]{t[1],t[0]+t[1]}).limit(n).map(t -> t[1]).reduce((a,b)-> a>b? a: b).get();
    }
}
