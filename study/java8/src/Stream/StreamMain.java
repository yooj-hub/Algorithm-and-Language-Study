package Stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static Stream.Dish.*;
import static Stream.Dish.Type.*;

public class StreamMain {
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
        List<String> threeHighCaloricDishNames =
                menu.stream()
                        .filter(dish -> dish.getCalories() > 300)
                        .sorted((a, b) -> b.getCalories() - a.getCalories())
                        .map(Dish::getName)
                        .limit(3)
                        .collect(Collectors.toList());
        System.out.println("threeHighCaloricDishNames = " + threeHighCaloricDishNames);

        List<String> names =
                menu.stream()
                        .map(Dish::getName)
                        .collect(Collectors.toList());
        System.out.println("names = " + names);

        List<String> highCaloricDishes =
                menu.stream()
                        .filter(d -> d.getCalories() > 300)
                        .map(Dish::getName)
                        .collect(Collectors.toList());
        System.out.println("highCaloricDishes = " + highCaloricDishes);

        long count =
                menu.stream()
                        .filter(d -> d.getCalories() > 300)
                        .distinct()
                        .limit(3)
                        .count();
        System.out.println("count = " + count);

        List<Dish> vegetarianDishes =
                menu.stream()
                        .filter(Dish::isVegetarian)
                        .collect(Collectors.toList());
        System.out.println("vegetarianDishes = " + vegetarianDishes);

        List<Integer> numbers = Arrays.asList(1, 2, 1, 3, 3, 2, 4);
        numbers.stream().filter(i -> i % 2 == 0).distinct().forEach(System.out::println);

        List<Dish> meats =
                menu.stream().filter(d -> d.getType() == MEAT).limit(2).collect(Collectors.toList());
        System.out.println("meats = " + meats);

        List<String> dishNames =
                menu.stream().map(Dish::getName).collect(Collectors.toList());
        System.out.println("dishNames = " + dishNames);
        List<String> words = Arrays.asList("Modern", "Java", "In", "Action");
        List<Integer> wordLengths =
                words.stream().map(String::length).collect(Collectors.toList());
        System.out.println("wordLengths = " + wordLengths);

        List<Integer> dishNameLengths =
                menu.stream().map(Dish::getName).map(String::length).collect(Collectors.toList());
        System.out.println("dishNameLengths = " + dishNameLengths);
        List<String[]> wordsByStream = words.stream().map(word -> word.split("")).collect(Collectors.toList());
        String[] arrayOfWords = {"Goodbye", "World"};
        List<String> uniqueCharacters = words.stream().map(a -> a.split("")).flatMap(Arrays::stream).distinct().collect(Collectors.toList());
        System.out.println("uniqueCharacters = " + uniqueCharacters);

    }
}
