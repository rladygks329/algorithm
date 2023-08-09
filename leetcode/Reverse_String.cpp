//problem_no : 344
//reverse() 함수이용
class Solution {
public:
    void reverseString(vector<char>& s) {
        reverse(s.begin(),s.end());
        return;
    }
};

/*
//swap() 함수이용
class Solution {
public:
    void reverseString(vector<char>& s) {
        int size = s.size();
        for(int i=0;i<size/2;i++){
            swap(s[i],s[size-1-i]);
        }
        
    }
};
*/

/*
class Solution {
public:
    void reverseString(vector<char>& s) {
        int size = s.size();
        char tmp;
        for(int i=0;i<size/2;i++)
        {
            tmp = s[i];
            s[i] = s[size-1-i];
            s[size-1-i] = tmp;
        }
    }
};
*/
