//problem : 160
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode* > set;
        pair<std::set<ListNode*>::iterator,bool> it;
        
        while(headA){
            it = set.insert(headA);
            headA = headA->next;
        }
        while(headB){
            it = set.insert(headB);
            if(it.second == false){
                return *it.first;
            }
            headB = headB->next;
        }
        return NULL;
    }
};
