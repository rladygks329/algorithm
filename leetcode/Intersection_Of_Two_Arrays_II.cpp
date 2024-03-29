//problem no : 350
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int i=nums1.size()-1,j=nums2.size()-1;
        vector<int> ans;
            
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        while(i>=0 && j>=0){
            if(nums1[i] == nums2[j]){
                ans.push_back(nums1[i]);
                i--;
                j--;
            }else if(nums1[i] < nums2[j]){
                j--;
            }else{
                i--;
            }
        }
        return ans;
    }
};
