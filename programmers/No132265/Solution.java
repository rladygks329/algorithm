package programmers.No132265;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Map<Integer, Integer> young = new HashMap<>();
        Map<Integer, Integer> old = new HashMap<>();

        for(int i=0; i<topping.length; i++){
            Integer count = old.get(topping[i]);
            old.put(topping[i], (count == null) ?  1 : count+1);
        }

        for(int i=0; i<topping.length; i++){
            Integer count = old.get(topping[i]);
            young.put(topping[i], 1);
            if (count == 1){
                old.remove(topping[i]);
            }else{
                old.put(topping[i], count - 1);
            }

            if(young.keySet().size() == old.keySet().size()){
                answer++;
            }
        }

        return answer;
    }
}

/*
[1, 2, 1, 3, 1, 4, 1, 2]
1. map 두개를 만든다
2. 한쪽은 비어있고 한쪽은 다 넣어놓는다 (토핑종류와 숫자를)
3. 원소를 돌면서 한쪽에 추가하고 한쪽에 뺀다.
4. 두 map의 원소를 비교해서 같으면 숫자를 늘린다.
*/