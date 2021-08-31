package Stream;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.util.Comparator.*;
import static java.util.stream.Collectors.*;

public class TraderAndTransaction {

    public static void main(String[] args) {
        Trader raoul = new Trader("Raoul", "Cambridge");
        Trader mario = new Trader("Mario", "Milan");
        Trader alan = new Trader("Alan", "Cambridge");
        Trader brian = new Trader("Brian", "Cambridge");

        List<Transaction> transactions = Arrays.asList(
                new Transaction(brian, 2011, 300),
                new Transaction(raoul, 2012, 1000),
                new Transaction(raoul, 2011, 400),
                new Transaction(mario, 2012, 710),
                new Transaction(mario, 2012, 700),
                new Transaction(alan, 2012, 950)
        );
        List<Trader> traders = transactions.stream().map(Transaction::getTrader).distinct().collect(toList());
        List<Transaction> first = transactions.stream().filter(d -> d.getYear() == 2011).sorted(comparing(Transaction::getValue)).collect(toList());
        List<String> second = traders.stream().map(Trader::getCity).distinct().collect(toList());
        List<String> third = traders.stream().filter(t -> t.getCity().equals("Cambridge")).map(Trader::getName).sorted(String::compareTo).collect(toList());
        List<String> fourth = traders.stream().map(Trader::getName).sorted(String::compareTo).collect(toList());
        boolean fifth = traders.stream().anyMatch(t -> t.getCity().equals("Milan"));
        Integer sixth = transactions.stream().filter(t -> t.getTrader().getCity().equals("Cambridge")).map(Transaction::getValue).reduce(0, Integer::sum);
        Integer seventh = transactions.parallelStream().map(Transaction::getValue).reduce(0, Integer::max);
        Integer eighth = transactions.parallelStream().map(Transaction::getValue).reduce(0, Integer::min);
        int k=1;
        Stream.iterate(new int[]{0, 1}, a -> new int[]{a[1], a[0] + a[1]}).limit(20).map(t -> t[0]).forEach( t-> System.out.print(t+" "));


    }

}
