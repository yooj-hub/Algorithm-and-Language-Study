# JAVA 8 함수형 인터페이스

> ​	함수형 인터페이스는 람다 표현식으로 함수형 인터페이스의 추상메서드 구현을 직접 전달할 수 있으므로 전체 표현식을 함수형 인터페이스의 인스턴스로 취급할 수 있다. (Modern Java In Action, 라울-게이브리얼 우르마 등 3명 ,한빛 미디어)

### 0. INIT

```java
        //init
        class NumberNode {

            public Integer number;

            public NumberNode(Integer number) {
                this.number = number;
            }

            public int getNumber() {
                return number;
            }
            public NumberNode() {

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
```







### 1. Predicate<T>

#### 	제네릭 변수를 받고, boolean 타입을 반환한다.

```java
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
///////////////////////////////////////////////////////////////////////////////////

    public static <T> List<T> filter(List<T> list, Predicate<T> p) {
        List<T> results = new ArrayList<>();
        for (T t : list) {
            if (p.test(t)) {
                results.add(t);
            }
        }
        return results;
    }
```





### 2. Consumer<T>

#### 	제네릭 변수를 받고, void 타입을 반환한다.

```java
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
///////////////////////////////////////////////////////////////////////////////
    public static <T> void forEach(List<T> list, Consumer<T> c) {
        for (T t : list) {
            c.accept(t);
        }
    }
```





### 3. Function<T, R>

#### 	제네릭 변수를 받고 제네릭 타입을 반환하는데, 반환타입이 지정 가능하다.



```java
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
////////////////////////////////////////////////////////////////////////////////
    public static <T> List<T> map(List<T> list, Function<T, T> f) {
        List<T> results = new ArrayList<>();
        for (T t : list) {
            results.add(f.apply(t));
        }
        return results;
    }
```





### 4. Comparator<T, T>

#### 	두 제네릭 변수를 비교해, 인트형을 반환한다.

```java
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
```



### 5. Supplier<T>

#### 	T 타입의 파라미터가 없는 Contructor 가 있을 경우 생성시 사용이 가능하다. 파라미터를 받아야 할 경우 Function을 써야한다.

```java
        System.out.println("----------  Supplier<T> ------------");

        Supplier<NumberNode> s = NumberNode::new;
        NumberNode numberNodeBySupplier = s.get();
        numberNodeBySupplier.number = 10;
        System.out.println("numberNodeBySupplier = " + numberNodeBySupplier);

        Function<Integer, NumberNode>f2 = NumberNode::new;
        NumberNode numberNodeByFunction = f2.apply(20);
        System.out.println("numberNodeByFunction = " + numberNodeByFunction);

        System.out.println("---------------------------------------");
```



전체 코드

```java
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

```



전체결과 ![funcInterface01](/Users/yujeongmin/Desktop/github/algorithm and simple study/study/java8/record/funcInterface01.png)

