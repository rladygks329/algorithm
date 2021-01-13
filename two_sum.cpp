class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        //정답을 위한 백터 선언
        vector<int> solution;

        //두번의 for문으로 주어진 배열에서 있는 모든 경우의 수를 찾기 위함
        //i = 1, j=2,3,4,5,6,7,8...end
        //i = 2, j=3,4,5,6,7,8,,end...
        //i = 3, j=4,5,6,7,8...end ...
        //i = end-1, j = end for문끝
        for(int i=0;i<nums.size()-1;i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums[i]+nums[j] == target)
                {
                    solution.push_back(i);
                    solution.push_back(j);
                    return solution;
                    //정답이 맞으면 두개의 루프를 탈풀하기 위해 break말고 return을쓴다
                }
            }
        }
        return solution;
    }
};
