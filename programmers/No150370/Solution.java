package programmers.No150370;

import java.util.ArrayList;
import java.util.HashMap;

public class Solution {
    public static void main(String[] args) {
        String today = "2022.05.19";
        String[] terms = {"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};

        int[] answer = solution(today,terms,privacies);
        for(int i : answer){
            System.out.println(i);
        }

    }
    public static int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> list = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();

        for(String term : terms){
            String[] tmp = term.split(" ");
            map.put(tmp[0], Integer.parseInt(tmp[1]));
        }

        for(int i=0; i<privacies.length; i++){
            String privacy =  privacies[i];
            String[] tmp = privacy.split(" ");
            int duration = map.get(tmp[1]);

            String[] s1 = today.split("\\.");
            String[] s2 = tmp[0].split("\\.");

            int[] diff = new int[3];
            diff[0] = Integer.parseInt(s1[0]) - Integer.parseInt(s2[0]) - duration/12;
            diff[1] = Integer.parseInt(s1[1]) - Integer.parseInt(s2[1]) - duration%12;
            diff[2] = Integer.parseInt(s1[2]) - Integer.parseInt(s2[2]) + 1;

            int diff_s1_s2 = diff[0] * 12 * 30 + diff[1] * 30 + diff[2];
            if(diff_s1_s2 > 0){
                list.add(i+1);
            }
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
