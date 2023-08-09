//problem no : 2
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int n = l1->val + l2->val;
        int roundUp = n/10;
        n %= 10;
        
        ListNode* ans = new ListNode(n);
        ListNode* i = ans;
        l1 = l1->next;
        l2 = l2->next;
        
        while(l1 && l2){
            n = l1->val + l2->val + roundUp;
            roundUp = n/10;
            n %= 10;
            i->next = new ListNode(n);
            i = i->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1){
            n = l1->val + roundUp;
            roundUp = n/10;
            n %= 10;
            i->next = new ListNode(n);
            i = i->next;
            l1 = l1->next;
        }
        while(l2){
            n = l2->val + roundUp;
            roundUp = n/10;
            n %= 10;
            i->next = new ListNode(n);
            i = i->next;
            l2 = l2->next;
        }
        if(roundUp){
            i->next = new ListNode(1);
        }
        return ans;
    }
};
