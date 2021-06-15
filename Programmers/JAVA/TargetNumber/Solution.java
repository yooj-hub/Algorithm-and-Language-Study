/*
 * Programmers TargetNumber
 * programmer: yooj
 * Date: 21.06.15
 * using: intellij & jdk 16.0.1
 * site: https://programmers.co.kr/learn/courses/30/lessons/43165
 */



import java.util.Arrays;

class Solution {
    static int answer=0;
    public static int solution(int[] numbers, int target) {
        Arrays.sort(numbers);
        int n = numbers.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += numbers[i];
        }
        int key = sum-target;
        if (key % 2 == 1 || key < 0)
            return -1;
        key /= 2;
        int j = n-1;
        for (; j >= 0; j--) {
            if (numbers[j] <= key) {
                break;
            }
        }
        while(j>=0){
            if(numbers[j]==key){
                answer++;
                j--;
            }
            else
                break;
        }
        while (j >= 0) {

                dfs(numbers,numbers[j],j,key);
                j--;
        }
        return answer;
    }
    public static void dfs(int[] numbers, int target,int depth,int key){
            if(key==target){
                answer++;
                return;
            }
            else if(target>key){
                return;
            }
            else if(depth==0){
                return;
            }
        dfs(numbers, target,depth-1,key);
        dfs(numbers, target+numbers[depth-1],depth-1,key);

    }
    public static void main(String[] args){
        int[] numbers={1,2,3,4,5};
        System.out.println(solution(numbers,9));
    }

}