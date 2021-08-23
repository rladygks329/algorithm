class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string commonPrefix = strs[0];
        
        if(strs.size() == 1)
            return commonPrefix;
        
        for(int i = 1; i <strs.size();i++)
        {
            int j = 0;
            while(strs[i][j] == commonPrefix[j])
            {
                if( j < commonPrefix.length())
                    j++;
                else 
                    break;
                
            }
            commonPrefix = commonPrefix.substr(0,j);
            if(commonPrefix =="") break;
        }
        return commonPrefix;
    }
};
