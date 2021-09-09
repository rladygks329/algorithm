//problem no : 136
/*class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i=0, s=nums.size()-1;
        while(i < s){
            if(nums[i] != nums[i+1]){
                return nums[i];
            }
            i+=2;
        }
        return nums[s];
    }
};
*/
class Solution {
    public:
        int singleNumber(vector<int>& nums){
            int ans = 0;
            for(int i=0;i<nums.size();i++){
                ans ^= nums[i];
            }
            return ans;
        }
};
