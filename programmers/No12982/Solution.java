package programmers.No12982;

import java.util.Arrays;

class Solution {
    public static int solution(int[] d, int budget) {
        int answer = 0;
        int i = 0;
        Arrays.sort(d);
        while(i < d.length && budget >= d[i]){
            answer += 1;
            budget -= d[i];
            i += 1;
        }
        return answer;
    }
}