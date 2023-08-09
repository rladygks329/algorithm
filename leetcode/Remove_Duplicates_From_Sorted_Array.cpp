class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int count = 1;
        for(int i=0; i<nums.size()-1;i++){
           if(nums[i] != nums[i+1])
           {
               nums[count] = nums[i+1];
               count++;
            }
        }
        return count;
    }
};
