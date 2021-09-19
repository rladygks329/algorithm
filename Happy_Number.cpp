//problem no : 202
class Solution {
public:
    int calHappy(int n){
        int ans = 0;
        while(n > 0){
            int i = n%10;
            ans +=  i*i;
            n /= 10;
        }
        return ans;
    }
    
    bool isHappy(int n) {
        int happyNum = calHappy(n);
        set<int> myset;
        pair<set<int>::iterator,bool> p;
        
        while(happyNum != 1){
            p = myset.insert(happyNum);
            if(p.second == false){
                return false;
            }
            happyNum = calHappy(happyNum);
        }
        
        return true;
    }
};
