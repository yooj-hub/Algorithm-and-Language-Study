/*
 * Programmers 네트워크
 * programmer: yooj
 * Date: 21.06.26
 * using: IntelliJ
 * Site: https://programmers.co.kr/learn/courses/30/lessons/43162
 */
public class Solution2 {
    private static boolean[] visited;//방문 체크를위한 visited
    public int solution(int n,int[][] computers){
        visited=new boolean[n];
        int answer=0;
        for(int i=0;i<n;i++){
            if(!visited[i]){//if문이 돌아갈 때 마다 answer을 1씩 추가
                dfs(computers, i);
                answer+=1;
            }

        }
        return answer;
    }

    public void dfs(int[][] computers,int start){
        visited[start]=true;//시작 노드 start
        for(int i=0;i<computers.length;i++){//모든 점에 대하여 실행
            if(computers[start][i]==1 && !visited[i]){
                dfs(computers,i);
            }
        }
    }
}
