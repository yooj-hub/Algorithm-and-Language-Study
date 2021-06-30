
/*
 * Programmers 이중우선순위 큐
 * programmer: yooj
 * Date: 21.06.30
 * using: IntelliJ
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42628
 */

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        PriorityQueue<Integer> q2 = new PriorityQueue<>(Collections.reverseOrder());
        int pp=0;

        for(int i=0;i<operations.length;i++){
            String[] tmp = operations[i].split(" ");
            if(tmp[0].equals("I")){
                q.add(Integer.parseInt(tmp[1]));
                q2.add(Integer.parseInt(tmp[1]));
                continue;
            }
            if(!q.isEmpty() && tmp[1].equals("-1")) {
                int temp1 = q.poll();
                q2.remove(temp1);
            }
            if(!q.isEmpty() && tmp[1].equals("1")){
                int temp = q2.poll();
                q.remove(temp);
            }

        }
        if(q.size()-pp<=0){
            return new int[]{0, 0};
        }
        int min = q.peek();
        int max=q2.peek();


        return new int[]{max,min};
    }
}