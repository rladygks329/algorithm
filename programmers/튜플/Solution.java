package programmers.튜플;

class Solution {
    public int[] solution(String s) {
        s = s.replace("{", "");
        s = s.substring(0, s.length() - 2);

        String[] arr = s.split("},");
        int[] answer = new int[arr.length];

        for(String s1: arr){
            String[] chars = s1.split(",");
            for(String s2: chars){
                answer[chars.length - 1] ^= Integer.parseInt(s2);
            }
        }

        for(int i=arr.length - 1; i > 0; i--){
            answer[i] ^= answer[i-1];
        }

        return answer;
    }
}