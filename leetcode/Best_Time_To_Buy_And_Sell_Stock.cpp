//problem no : 121
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int s = prices[0];
        int ans = 0;
        
        for(int p : prices){
            s = min(s, p);
            ans = max(ans, p-s);
        }
        return ans;
    }
};
