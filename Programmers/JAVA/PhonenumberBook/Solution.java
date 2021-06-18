/*
 * Programmers 전화번호 목록
 * programmer: yooj
 * Date: 21.06.19
 * using: IntelliJ & jdk.16.0.1
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42577
 */

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;

class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> hs = new HashSet<>();//Hashset hs선언
        int n = phone_book.length;//phon book배열의 길이
        boolean answer = true;
        Arrays.sort(phone_book, new Comparator<String>() {//new Comparator<String>()을 통해 길이순으로 배열
            @Override
            public int compare(String o1, String o2) {
                return Integer.compare(o1.length(), o2.length());
            }
        });
        int k = 0;
        for (int j = 0; j < n - 1; j++) {
            hs.add(phone_book[j]);//hs에 j번째 phone_book추가
            k = phone_book[j].length();//j번째 phone_book의 길이를 k에 저장
            for (int i = j + 1; i < n; i++) {
                int l = phone_book[i].length();
                if (k == l) {//i번째와 j번째가 길이가 같으면 모든 번호가 다르므로 서로 무조건 다르다
                    hs.add(phone_book[i]);//i번쨰 번호를 추가
                    j++;//다음 j번째를 생략하기위한 연산
                }
                if (k < l) {//k<l일 경우 접두어인 경우가 발생할 수 있다.
                    answer = !(hs.contains(phone_book[i].substring(0, k)));//substring 을 포함하는 지 확인
                    if (!answer)////answer이 false이면 종료
                        break;
                }
            }
            if (!answer)//answer이 false이면 종료
                break;
        }
        return answer;//answer 반환
    }


}