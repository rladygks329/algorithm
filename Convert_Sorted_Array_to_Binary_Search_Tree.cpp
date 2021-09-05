/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int size = nums.size();
        return makeBST(nums, 0, size);
    }
    TreeNode* makeBST(vector<int>& nums, int start, int end){
        if(start >= end) return NULL;
        int middle = (start + end)/2;
        TreeNode* curr = new TreeNode(nums[middle]);
        curr->left = makeBST(nums, start, middle);
        curr->right = makeBST(nums, middle+1,end);
        return curr;
    }
};

