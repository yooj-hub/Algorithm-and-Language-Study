package Stream;

import java.util.Arrays;
import java.util.List;

import static java.util.stream.Collectors.toList;

public class StreamQuiz {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> squaredNumbers
                = numbers.stream()
                .map(n -> n * n).collect(toList());
        System.out.println("squaredNumbers = " + squaredNumbers);

        List<Integer> numbers1 = Arrays.asList(1, 2, 3);
        List<Integer> numbers2 = Arrays.asList(3, 4);
        List<int[]> pairs = numbers1.stream().flatMap(i -> numbers2.stream()
                .map(j -> new int[]{i, j})).collect(toList());
        for (int[] pair : pairs) {
            System.out.println("pair[0]= " + pair[0] + " pair[1]= " + pair[1]);
        }
        System.out.println("============================================");
        List<int[]> three = numbers1.stream()
                .flatMap(i -> numbers2.stream()
                        .filter(j -> (i + j) % 3 == 0)
                        .map(j -> new int[]{i, j})
                )
                .collect(toList());
        for (int[] ints : three) {
            System.out.println("ints[0]= " + ints[0] + " ints[1]= " + ints[1]);
        }
    }
}
