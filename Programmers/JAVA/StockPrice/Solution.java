/*
 * Programmers Stock Price
 * programmer: yooj
 * using : intellij & jdk 16.0.2
 * Date: 21.06.14
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42584
 */

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer=new int[n];
        for(int i=0;i<n;i++){
            answer[i]=check(i,n,prices);
        }
        answer[n-1]=0;
        return answer;
    }
     int check(int left, int right, int[] a) {
        int j = 1;
        for (int i = left + 1; i < right-1; i++) {
            if (a[left] <= a[i])
                j++;
            else
                break;
        }
        return j;
    }
}

