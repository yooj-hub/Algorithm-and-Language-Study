/*
 * Programmers 프린터
 * programmer: yooj
 * Date: 21.06.20
 * using: IntelliJ & jdk.16.0.1
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42587
 */

import java.util.ArrayList;

class Solution {
    public  int solution(int[] priorities, int location) {
        int answer = 0;
        int n = priorities.length;
        Node[] s= new Node[n];
        ArrayList<Node> nl = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nl.add(new Node(i,priorities[i]));//arraylist에 우선순위와 고유번호 저장
        }
        while(!nl.isEmpty()){//arrayList가 존재하면
            boolean change= false;//바꿀지 말지 정하는 boolean 변수
            int k = nl.get(0).pri;//첫 번째 노드의 우선순위
            for(int x=k+1;x<10;x++){//첫번째 노드보다 큰 우선순위를 갖는게 있는지 탐색
                for(int c=1;c<nl.size();c++){//arraylist의 사이즈만큼 탐색
                    if(nl.get(c).pri==x) {//있으면
                        change = true;//change = true
                        break;//break
                    }
                    if(change)
                        break;//break
                }
            }
            if(change){//바꿀경우
                nl.add(nl.get(0));//처음 것을 마지막에추가
                nl.remove(0);//처음 것을 제거
            }
            else{
                if(nl.get(0).cus==location){//바꾸지 않고, 처음에 있는게 target일 경우
                    return answer+1;//answer+1을 리턴(1부터 이므로)
                }
                nl.remove(0);//만약 target이아니면 처음에 있는것 제거
                answer++;//하나가 프린트 됐으므로 answer+1
            }

        }
        return answer;
    }

    public class Node {//우선순위와 고유번호를 저장하기위한 Node
        int cus;//고유번호
        int pri;//우선순위

        Node(int cus, int pri) {//생성자
            this.cus = cus;
            this.pri = pri;
        }
    }

}