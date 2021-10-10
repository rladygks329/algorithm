//problem no: 3 
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string sub = "";
        int start = 0;
        int m = 0;
        
        for(int i=0;i<s.size();i++){
            for(int j=start;j<sub.size();j++){
                if(s[i] == sub[j]){
                    m = max(m, i-start);
                    start = j+1;
                }        
            }
            sub.push_back(s[i]);
        }
        if(m < s.size()-start){
            m = s.size() - start;
        }
        return m;
    }  
};
