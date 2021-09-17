package Stream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static Stream.Dish.Type.*;
import static Stream.Dish.Type.FISH;
import static java.util.stream.Collectors.*;

public class Grouping {
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

    public static void main(String[] args) {
        Map<Dish.Type, List<Dish>> collect = menu.stream().collect(groupingBy(Dish::getType));
        System.out.println("collect = " + collect);
        for (Dish.Type type : collect.keySet()) {
            System.out.println("type = " + type);

        }
        for (List<Dish> value : collect.values()) {
            System.out.println("value = " + value);
        }
        Map<Dish.Type, List<String>> collect1 = menu.stream().filter(d -> d.getCalories() > 500).collect(groupingBy(Dish::getType, mapping(Dish::getName, toList())));
        System.out.println("collect1 = " + collect1);
    }
}
