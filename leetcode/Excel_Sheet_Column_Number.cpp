class Solution {
public:
    int titleToNumber(string columnTitle) {
        int count = 0;
        for(int i=0;i<columnTitle.size();i++){
            count += alphaTransfer(columnTitle[i]) * pow(26,columnTitle.size()-1-i);
        }
        return count;
    }
    int alphaTransfer(char c){
        return (int)c -64;
    }
};
