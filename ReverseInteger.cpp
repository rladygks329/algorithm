class Solution {
public:
    int reverse(int x) {
        bool signX = false;
        if(x < 0 && x != INT_MIN){ signX = true; x *= -1;}
        
        int answer = 0;
        while( x > 0)
        {
            if( answer <=  INT_MAX /10)
            {   
                answer *= 10;
                answer += x%10;
                x /= 10;
            }
            else 
                return 0;
        }
        return signX ? answer * -1 : answer;
        
    }
};
