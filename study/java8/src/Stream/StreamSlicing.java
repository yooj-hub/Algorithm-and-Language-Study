package Stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static Stream.Dish.Type.*;

public class StreamSlicing {
    static List<Dish> specialMenu = Arrays.asList(
            new Dish("seasonal fruit", true, 120, OTHER),
            new Dish("prawns", false, 300, FISH),
            new Dish("rice", true, 350, OTHER),
            new Dish("chicken", false, 400, MEAT),
            new Dish("french fries", true, 530, OTHER)
    );

    public static void main(String[] args) {
        List<Dish> filteredMenu =
                specialMenu.stream()
                        .filter(d -> d.getCalories() < 320)
                        .collect(Collectors.toList());
        System.out.println("filteredMenu = " + filteredMenu);

        //리스트가 정렬되어 있을경우 takeWhile 이용
        List<Dish> sliceMenu1
                = specialMenu.stream()
                .takeWhile(d -> d.getCalories() < 320)
                .collect(Collectors.toList());
        System.out.println("sliceMenu1 = " + sliceMenu1);

        //리스트가 정렬되어 있을 때 반대 결과는 dropWhile 이용
        List<Dish> sliceMenu2
                = specialMenu.stream()
                .dropWhile(d -> d.getCalories() < 320)
                .collect(Collectors.toList());
        System.out.println("sliceMenu2 = " + sliceMenu2);

        List<Dish> dishes = specialMenu.stream()
                .filter(dist -> dist.getCalories()>300)
                .limit(3)
                .collect(Collectors.toList());
        System.out.println("dishes = " + dishes);



    }

}
