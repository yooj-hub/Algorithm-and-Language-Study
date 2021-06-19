/*
 * Programmers 베스트 앨범
 * programmer: yooj
 * Date: 21.06.20
 * using: IntelliJ & jdk.16.0.1
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42579
 */

import java.util.*;

class Solution {

    public int[] solution(String[] genres, int[] plays) {
        int n = genres.length;
        HashSet<String> hs = new HashSet<>();//genre중 제일 재생수 많은것을 얻기위한 hashset
        ArrayList<Node> nal = new ArrayList<>();
        ArrayList<Integer> il = new ArrayList<>();
        Node2[] n2l = new Node2[n];//고유번호를 포함한 Node
        for (int i = 0; i < n; i++) {//Node2와 Node ArrayList에 각각 추가
            n2l[i] = new Node2(genres[i], plays[i], i);
            if (hs.add(genres[i])) {
                nal.add(new Node(genres[i], plays[i]));//같은 장르가 없으면 새롭게 추가
            } else {
                setPlays(nal, genres[i], plays[i]);//있으면 setPlays를 통해 기존의 plays에 plays를 더함
            }
        }

        Node[] nl = new Node[nal.size()];//node는 장르별 play수를 가진 node임
        for (int i = 0; i < nal.size(); i++) {
            nl[i] = new Node(nal.get(i).genres, nal.get(i).plays);
        }

        Arrays.sort(nl, new Comparator<Node>() {//play순으로 오름차순 배열
                    @Override
                    public int compare(Node o1, Node o2) {
                        return Integer.compare(o1.plays, o2.plays);
                    }
                }
        );

        Arrays.sort(n2l, new Comparator<Node2>() {//play순으로 장르와 상관없이 정렬
            @Override
            public int compare(Node2 o1, Node2 o2) {
                return o1.plays > o2.plays ? -1 : 1;// 오름차순 정렬
            }
        });

        for (int i = nl.length - 1; i >= 0; i--) {//제일 play가 많은 순으로 탐색
            String pick = nl[i].genres;//제일 플레이가 많은 장르를 pick에 저장
            int q = 0;//총 저장되는 개수
            {
                for (int j = 0; j < n; j++) {
                    if (pick.equals(n2l[j].genres)) {//같은 장르이면
                        il.add(n2l[j].cus);//int arrayList에 고유번호 추가
                        q++;
                    }
                    if (q == 2)// 2개가 저장되면 정지
                        break;
                }
            }
        }
        int[] answer = new int[il.size()];//il 사이즈만큼 설정
        for (int i = 0; i < il.size(); i++) {//arrayList에 있는것을 answer에 복사
            answer[i] = il.get(i);
        }
        return answer;//리턴
    }

    public void setPlays(ArrayList<Node> asl, String str, int plays) {
        for (int i = 0; i < asl.size(); i++) {
            if (asl.get(i).genres.equals(str)) {//같은 장르를 찾아서 추가함
                asl.get(i).plays += plays;
            }
        }
    }


    class Node {//장르와 play를 저장하는 노드
        String genres;
        int plays;

        Node(String genres, int plays) {
            this.genres = genres;
            this.plays = plays;
        }
    }

    class Node2 {//장르와 play와 고유번호를 저장하는 노드
        String genres;
        int plays;
        int cus;

        Node2(String genres, int plays, int cus) {
            this.genres = genres;
            this.plays = plays;
            this.cus = cus;

        }
    }


}