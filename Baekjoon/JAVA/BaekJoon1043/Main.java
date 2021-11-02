/**
 * BaekJoon 1043 거짓말
 * programmer: yooj
 * Date: 21.11.02
 * using: Intellij & jdk 16.0.2
 * Site: https://www.acmicpc.net/problem/1043
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    // 노드의 부모를 저장할 parent 배열
    private static final int[] parent = new int[51];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        List<Integer> partyPeopleAndPartyNumber = getIntegers(br);
        // 지민이를 제외한 인원 수
        int n = partyPeopleAndPartyNumber.get(0);
        // 총 파티 수
        int m = partyPeopleAndPartyNumber.get(1);
        // 부모 초기화
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        SizeAndList lies = getSizeAndList(br);
        for (int i = 0; i < lies.size; i++) {
            // 거짓말을 한 사람의 부모를 0 으로 변경
            parent[lies.list.get(i)] = 0;
        }
        // party 를 대표할 인원을 저장하는 ArrayList
        List<Integer> partiesParent = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            // party 의 수와 party 참여 인원을 입력받음
            SizeAndList parties = getSizeAndList(br);
            partiesParent.add(parties.list.get(0));
            for (int j = 0; j < parties.size - 1; j++) {
                unionParent(parties.list.get(j), parties.list.get(j + 1));
            }
        }
        // 거짓말을 알고 있는 사람을 포함하지 않은 파티수를 구함
        bw.write(Long.toString(partiesParent.stream().filter(a -> findParent(a) != 0).count()));
        bw.flush();

    }

    // 부모를 찾는 method
    private static int findParent(int x) {
        if (parent[x] == x) {
            return parent[x];
        }
        parent[x] = findParent(parent[x]);
        return parent[x];
    }

    // 합치는 method 낮은 것을 기준으로
    private static void unionParent(Integer integer, Integer integer1) {
        int a = findParent(integer);
        int b = findParent(integer1);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }

    }

    // 입력을 위한 함수
    private static List<Integer> getIntegers(BufferedReader br) throws IOException {
        return Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
    }

    private static SizeAndList getSizeAndList(BufferedReader br) throws IOException {
        List<Integer> list = getIntegers(br);
        SizeAndList sizeAndList = new SizeAndList();
        for (int i = 0; i < list.size(); i++) {
            if (i == 0) {
                sizeAndList.size = list.get(i);
                continue;
            }
            sizeAndList.list.add(list.get(i));
        }
        return sizeAndList;
    }

    // size 와 List 를 가진 클래스
    private static class SizeAndList {
        int size;
        List<Integer> list = new ArrayList<>();
    }
}
