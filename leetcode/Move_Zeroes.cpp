//problem no : 283
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int index = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]){
                swap(nums[index++], nums[i]);
            }
        }
    }
};
