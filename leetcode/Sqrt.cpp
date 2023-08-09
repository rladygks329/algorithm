class Solution {
public:
    int mySqrt(int x) {
        if(x == 0) return 0;
        if(x > 2147395600) return 46340;
        int sqr = 1, i = 1; 
        while(sqr < x)
        {
            sqr = sqr + 2*i +1;
            if(sqr > x)
            {
                break;
            }
            i++;
        }
        return i;
    }
};
