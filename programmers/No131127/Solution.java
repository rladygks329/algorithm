package programmers.No131127;

import java.util.HashMap;
import java.util.Optional;

class Solution {
    public static void main(String[] args) {
        String[] want = {"banana", "apple", "rice", "pork", "pot"};
        int[] number = {3, 2, 2, 2, 1};
        String[] discount = {"chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"};
        System.out.println(solution(want, number, discount));
    }

    public static int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        //set
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            map.put(want[i], i);
        }

        for (int i = 0; i < discount.length; i++) {
            Optional.ofNullable(map.get(discount[i]))
                    .ifPresent(integer -> number[integer] -= 1);

            boolean valid = true;
            for (int j = 0; j < number.length; j++) {
                if (number[j] > 0) {
                    valid = false;
                    break;
                }
            }
            answer += (valid) ? 1 : 0;

            if (i >= 9) {
                Optional.ofNullable(map.get(discount[i - 9]))
                        .ifPresent(integer -> number[integer] += 1);
            }
        }
        return answer;
    }
}
