//problem no: 141
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        while(fast && fast->next ){
            head = head->next;
            fast = fast->next->next;
            if(head == fast) return true;
        }
        return false;     
    }
};
