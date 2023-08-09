class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;       
        vector<int> cur(1,1);
        for(int i=1;i<=numRows;i++){
            vector<int> next(i,1);
            for(int j=1;j<i-1;j++){
                next[j] = cur[j-1] + cur[j];
            }
            ans.push_back(next);
            cur.swap(next);
        }
        return ans;
    }
    
};
