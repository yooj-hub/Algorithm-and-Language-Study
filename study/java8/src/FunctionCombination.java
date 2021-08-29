import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

import static java.util.Comparator.comparing;

public class FunctionCombination {
    public static void main(String[] args) {
        /**
         * Predicate
         * Supplier
         * Consumer
         * Function
         * Comparator
         */
        //init
        class NumberNode {


            public Integer number;

            public NumberNode(Integer number) {
                this.number = number;
            }

            public NumberNode() {

            }

            public int getNumber() {
                return number;
            }

            @Override
            public String toString() {
                return "NumberNode{" +
                        "number=" + number +
                        '}';
            }
        }
        List<Integer> list = new ArrayList<>();
        List<NumberNode> numberNodeList = new ArrayList<>();
        for (int i = 1; i <= 20; i++) {
            list.add(i);
            numberNodeList.add(new NumberNode(i));
        }
        System.out.println("--------------  Predicate<T>  ------------");
        System.out.println("return type is boolean");

        System.out.println("Predicate<Integer> integerPredicate = x -> x > 10");
        Predicate<Integer> integerPredicate = x -> x > 10;

        boolean falseResultParamIs5 = integerPredicate.test(5);
        boolean trueResultParamIs20 = integerPredicate.test(20);

        System.out.println("falseResultParamIs5 = " + falseResultParamIs5);
        System.out.println("trueResultParamIs20 = " + trueResultParamIs20);

        List<Integer> filteredList = filter(list, integerPredicate);
        System.out.println("filteredList = " + filteredList);

        System.out.println("---------------------------------------");

        System.out.println("--------------  Consumer<T>  -------------");
        System.out.println("return type is void");

        System.out.println("Consumer<Integer> c = x -> System.out.print(x + \" \")");
        Consumer<Integer> c = x -> System.out.print(x + " ");

        c.accept(10);
        c.accept(20);
        System.out.println();

        forEach(list, c);
        System.out.println();

        System.out.println("---------------------------------------");

        System.out.println("-----------  Function<T, R> -----------");
        System.out.println("return type is R");

        System.out.println("Function<Integer, Integer> f = x -> x + 1");
        System.out.println("Function<Integer, Integer> g = x -> x * 2");
        System.out.println("Function<Integer, Integer> h = f.andThen(g)");
        System.out.println("Function<Integer, Integer> i = f.compose(g)");
        Function<Integer, Integer> f = x -> x + 1;
        Function<Integer, Integer> g = x -> x * 2;
        Function<Integer, Integer> h = f.andThen(g);
        Function<Integer, Integer> i = f.compose(g);

        int resultFParamIs1 = f.apply(1);
        int resultGParmaIs2 = g.apply(2);
        int resultHParamIs3 = h.apply(3);
        int resultIParamIs4 = i.apply(4);
        System.out.println("resultFParamIs1 = " + resultFParamIs1);
        System.out.println("resultGParmaIs2 = " + resultGParmaIs2);
        System.out.println("resultHParamIs3 = " + resultHParamIs3);
        System.out.println("resultIParamIs4 = " + resultIParamIs4);

        List<Integer> mappedList = map(list, f);
        System.out.println("mappedList = " + mappedList);

        System.out.println("---------------------------------------");

        System.out.println("----------  Comparator<T, T> ----------");
        System.out.println("Comparator is (a1, a2) -> a2 - a1");
        System.out.println("comparing(Object::func)");
        list.sort((a1, a2) -> a2 - a1);

        System.out.println("numberNodeList = filter(numberNodeList, n -> n.getNumber() > 15)");
        System.out.println("numberNodeList.sort(comparing(NumberNode::getNumber).reversed())");
        numberNodeList = filter(numberNodeList, n -> n.getNumber() > 15);
        numberNodeList.sort(comparing(NumberNode::getNumber).reversed());

        System.out.println("list = " + list);
        System.out.println("numberNodeList = " + numberNodeList);

        System.out.println("---------------------------------------");

        System.out.println("----------  Supplier<T> ------------");

        Supplier<NumberNode> s = NumberNode::new;
        NumberNode numberNodeBySupplier = s.get();
        numberNodeBySupplier.number = 10;
        System.out.println("numberNodeBySupplier = " + numberNodeBySupplier);

        Function<Integer, NumberNode>f2 = NumberNode::new;
        NumberNode numberNodeByFunction = f2.apply(20);
        System.out.println("numberNodeByFunction = " + numberNodeByFunction);

        System.out.println("---------------------------------------");
    }


    public static <T> List<T> filter(List<T> list, Predicate<T> p) {
        List<T> results = new ArrayList<>();
        for (T t : list) {
            if (p.test(t)) {
                results.add(t);
            }
        }
        return results;
    }

    public static <T> void forEach(List<T> list, Consumer<T> c) {
        for (T t : list) {
            c.accept(t);
        }
    }

    public static <T> List<T> map(List<T> list, Function<T, T> f) {
        List<T> results = new ArrayList<>();
        for (T t : list) {
            results.add(f.apply(t));
        }
        return results;
    }


}
