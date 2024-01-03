package programmers.기능개발;

import java.util.ArrayList;


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int size = progresses.length;
        for(int i = 0; i < size; i++){
            progresses[i] = (int) Math.ceil((double)(100 - progresses[i])/speeds[i]);
        }

        ArrayList<Integer> arr = new ArrayList<>();
        int count = 1;
        int prev = progresses[0];
        for(int i = 1; i < size; i++){
            if(prev >= progresses[i]){
                count += 1;
            }else{
                arr.add(count);
                prev = progresses[i];
                count = 1;
            }
        }
        arr.add(count);
        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
}