class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        unordered_map<int, int> m;
        for(int i =0; i<nums.size();i++){
            if(m.find(nums[i]) != m.end()){
                answer.push_back(m[nums[i]]);
                answer.push_back(i);
                return answer;
            }
            m[target - nums[i]] = i;
        }
        return answer;
    }
};
