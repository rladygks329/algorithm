//problem no : 234
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        int count = 0;
        ListNode* prev = NULL; 
        ListNode* cur = head;
        ListNode* next = head->next;
        
        while(head){
            count++;
            head = head->next;
        }
        for(int i=0;i<(count+1)/2;i++){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        } 
        
        if(count%2 == 1){
            prev = prev->next;
        }
        
        while(cur){
            if(cur->val != prev->val){
                return false;
            }
            cur = cur->next;
            prev = prev->next;
        }
        return true;
    }
};
