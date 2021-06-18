/*
 * Programmers 완주하지 못한 선수
 * programmer: yooj
 * Date: 21.06.18
 * using: IntelliJ & jdk.16.0.1
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42576
 */

import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);//sort
        Arrays.sort(completion);//sort
        int ans=Arrays.mismatch(participant,completion);//missmatch 메소드는 처음으로 다른 인덱스를 리턴함
        return participant[ans];//답
    }


}
