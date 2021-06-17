//Stack.java

public class Stack<E> {//제네릭 클래스 stack
    private int max;//최대 입력가능한 개수
    private int ptr;//위치를 표시하는 포인터
    private E[] stk;//데이터를 저장할 배열
    private int size;//현재 스택에 저장된 개수

    //예최 처리
    public static class EmptyEStackException extends RuntimeException{
        public EmptyEStackException(){}
    }
    public static class OverflowEStackException extends RuntimeException{
        public OverflowEStackException(){}
    }

    //Constructor
    public Stack(int capacity){
        ptr=0;
        max= capacity;
        size=0;
        stk= (E[]) new Object[max];
        System.out.println("용량이 "+capacity+"인 스택이 생성되었습니다.");
    }
    //Push 스택에 저장
    public E push(E x) throws OverflowEStackException{
        if(ptr>=max)
            throw new OverflowEStackException();
        size++;
        System.out.println("현재 저장된 자료의 개수는 "+size+"개 입니다.");
        return stk[ptr++]=x;
    }
    //Pop 스택에 가장 쵠근에 저장된 것을 꺼냄
    public E pop() throws EmptyEStackException{
        if(ptr<=0)
            throw new EmptyEStackException();
        size--;
        return stk[--ptr];
    }
    //Peek or Top 스택에서 꺼내질 내용물을 확인
    public E peek() throws EmptyEStackException{
        if(ptr<=0)
            throw new EmptyEStackException();
        return stk[ptr-1];

    }
    //스택에 x가 존재하는지 확인
    public int indexOf(E x){
        for(int i=ptr-1;i>=0;i--){
            if(stk[i]==x){
                return i;
            }
        }
        return -1;
    }
    //스택 삭제
    public void clear(){
        System.out.println("스택이 지워졌습니다");
        ptr=0;
    }
    //스택의 용량 확인
    public int capacity(){
        return capacity();
    }
    //스택의 현재 저장된 자료의 개수 확인
    public int size(){
        return size;
    }
    //스택이 비었는지 확인
    public boolean isEmpty(){
        return ptr<=0;
    }
    //스택이 가득차있는지 확인
    public boolean isFull(){
        return ptr>=max;
    }



}

