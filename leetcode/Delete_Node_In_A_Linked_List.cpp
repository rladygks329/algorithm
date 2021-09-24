/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        *node =*(node->next);
    }
};

/*
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* right = node->next;
        node->val = right->val;
        node->next = right->next;
        delete right;
    }
};
*/
