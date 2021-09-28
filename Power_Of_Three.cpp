//problem no : 326
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<1) return false;
        
        while(n%3 == 0){
            n/=3;
        }
        
        return n == 1;
    }
};

/*
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(!n) return false;
        double a = log10(n)/log10(3);
        return floor(a) == a;    
    }
};
*/
