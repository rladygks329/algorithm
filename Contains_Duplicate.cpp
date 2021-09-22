//problem no : 217
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        bool result = false;
        
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<nums.size()-1; i++){
            
            if(nums[i] == nums[i+1]) {
                result = true;
                break;
            } 
        }
        return result;
    } 
   
};

/*class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        
        for(int i=0; i<nums.size();i++){
            pair<set<int>::iterator, bool> tmp = s.insert(nums[i]);
            if(tmp.second == false) return true;
        }
        return false;
    }
};*/
