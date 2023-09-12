package programmers.No84512;

public class Solution {
    private static int answer;
    private static int count;
    private char[] vowels = {'A', 'E', 'I', 'O', 'U'};
    private StringBuilder sb = new StringBuilder();
    public static void main(String[] args) {

    }
    public int solution(String word) {
        helper(0, word);
        return answer;
    }
    public void helper(int n, String word){
        if(n == 5){
            return;
        }

        for(int i=0; i<5; i++) {
            sb.append(vowels[i]);
            count++;
            if (word.equals(sb.toString())) {
                answer = count;
            }
            helper(n + 1, word);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
