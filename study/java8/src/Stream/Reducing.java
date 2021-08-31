package Stream;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import static Stream.Dish.Type.*;
import static Stream.Dish.Type.FISH;

public class Reducing {
    static List<Dish> menu = Arrays.asList(
            new Dish("pork", false, 800, MEAT),
            new Dish("beef", false, 700, MEAT),
            new Dish("chicken", false, 400, MEAT),
            new Dish("french fries", true, 530, OTHER),
            new Dish("rice", true, 350, OTHER),
            new Dish("season fruit", true, 120, OTHER),
            new Dish("pizza", true, 550, OTHER),
            new Dish("prawns", false, 300, FISH),
            new Dish("salmon", false, 450, FISH)
    );
    static List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

    public static void main(String[] args) {

        System.out.println(numbers.stream().reduce(0, Integer::sum));
        numbers.stream().reduce(Integer::sum).ifPresent(a -> System.out.println("sumOfNumbers = " + a));

        Optional<Integer> max = numbers.stream().reduce(Integer::max);
        max.ifPresent(a -> System.out.println("maxNumber = " + a));

        Integer count = menu.stream().map(d -> 1).reduce(0, Integer::sum);
        System.out.println("count = " + count);


    }
}
