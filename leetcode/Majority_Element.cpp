// problem no : 169
/*class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> m;
        for(int i=0;i<nums.size()/2;i++){
            m[nums[i]] += 1;
        }
        for(int i=nums.size()/2;i<nums.size();i++){
            m[nums[i]] += 1;
            if(m[nums[i]] > nums.size()/2){
                return nums[i];
            }
        }
        return -1;
    }
};*/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major = nums[0], count = 1;
        for(int i=1;i<nums.size();i++){
            if(major == nums[i]){ count++;}
            else{
                count--;
                if(count == 0){ major = nums[i]; count++;} 
            }
            
        }
        return major;
    }
};
