class Solution {
public:
    int romanToInt(string s) {
        int answer = 0;
        int signOne = 1;
        int signTen = 1;
        int signHun = 1;
        
        for(int i = s.size(); i > -1; i--){
            switch(s[i])
            {
                case 'I':
                    answer += signOne * 1;
                    break;
                case 'V':
                    answer += 5;
                    signOne = -1;
                    break;
                case 'X':
                    answer += signTen * 10;
                    signOne = -1;
                    break;
                case 'L':
                    answer += 50;
                    signTen = -1;
                    break;
                case 'C':
                    answer += signHun * 100;
                    signTen = -1;
                    break;
                case 'D':
                    answer += 500;
                    signHun = -1;
                    break;
                case 'M':
                    answer += 1000;
                    signHun = -1;
                    break;
            }
        }
        return answer;
    }
};
