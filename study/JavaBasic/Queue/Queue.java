/*
 * Queue 구현
 * programmer: yooj
 * Date: 21.06.22
 * using: IntelliJ & jdk.16.0.1
 */
public class Queue<E> {
    private int size;
    private int max;
    private int first;
    private int last;
    private E[] items;

    Queue(int capacity) {
        this.size = 0;
        this.max = capacity;
        this.first = 0;
        this.last = 0;
        this.items = (E[]) new Object[max];
        System.out.println("큐가 생성되었습니다.");
    }

    public static class EmptyEQueueException extends RuntimeException {
        public EmptyEQueueException() {
            System.out.println("Queue is Empty");
        }
    }

    public static class OverflowEQueueException extends RuntimeException {
        public OverflowEQueueException() {
            System.out.println("Queue is Full");
        }
    }

    public E add(E a) throws OverflowEQueueException {
        if (size >= max) {
            throw new OverflowEQueueException();
        }
        items[last++] = a;
        size++;
        if (last == max) {
            last = 0;
        }
        return a;
    }

    public E pop() throws EmptyEQueueException {
        if (size <= 0) {
            throw new EmptyEQueueException();
        }
        size--;
        last--;
        return items[first++];
    }
    public E peek() throws EmptyEQueueException{
        if(size<=0){
            throw new EmptyEQueueException();
        }
        return items[first];
    }
    public boolean isEmpty(){
        return size<=0;
    }
    public boolean isFull(){
        return size>=max;
    }
    public void clean(){
        last=0;
        first=0;
        size=0;
    }
    public int size(){
        return size;
    }
    public int indexOf(E a){
        for(int i=first; i<last;i++){
            if(items[i]==a)
                return i;
        }
        return -1;
    }
}
