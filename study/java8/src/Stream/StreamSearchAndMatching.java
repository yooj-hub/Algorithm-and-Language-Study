package Stream;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static Stream.Dish.Type.*;
import static Stream.Dish.Type.FISH;

public class StreamSearchAndMatching {
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
        if (menu.stream().anyMatch(Dish::isVegetarian)) {
            System.out.println("The menu is (somewhat) vegetarian friendly!");
        }
        boolean isHealthy = menu.stream().allMatch(a -> a.getCalories() < 1000);
        System.out.println("isHealthy = " + isHealthy);

        boolean isHealthy2 = menu.stream().noneMatch(d -> d.getCalories() > 1000);
        System.out.println("isHealthy2 = " + isHealthy2);

        menu.stream().filter(Dish::isVegetarian).findAny().ifPresent(d -> System.out.println("d.getName() = " + d.getName()));


    }

}
