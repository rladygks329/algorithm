class Solution {
public:
    int climbStairs(int n) {
        int prev = 1, current = 1;
        for(int i = 1; i<n; i++)
        {
            int tmp = current;
            current = prev + current;
            prev = tmp;
        }
        return current;
    }
};
