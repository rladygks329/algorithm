package programmers.No12930;


import java.util.ArrayList;

class Solution {
    public static void main(String[] args) {
        String s = "try hello world";
        String answer = solution(s);
        System.out.println(answer);
    }
    public static String solution(String s) {
        // split에서 마지막 공백 문자를 포함하도록 limit를 준다.
        String[] arr = s.toLowerCase().split(" ", -1);
        ArrayList<String> answer = new ArrayList<>();

        for(String s1: arr){
            StringBuilder sb = new StringBuilder();
            for(int i=0; i<s1.length(); i++){
                char c = s1.charAt(i);
                sb.append((i%2 == 0) ? Character.toUpperCase(c) : c );
            }
            answer.add(sb.toString());
        }

        return String.join(" ", answer);
    }
}
