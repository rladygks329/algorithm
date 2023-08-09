//problem no : 242
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length() != t.length()){return false;}
        
        int ans[26] = {0,};
        for(int i=0;i<s.length();i++){
            ans[s[i]-'a'] += 1;
            ans[t[i]-'a'] -= 1;
        }
        for(int i: ans){
            if(i){
                return false;
            }
        }
        return true;
    }
};
