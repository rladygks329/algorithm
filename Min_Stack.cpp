//problem no: 155
class MinStack {
public:
    /** initialize your data structure here. */
    int minimum = INT_MAX;
    int numberOfEntries= 0;
    int* s;
    int capacity = 1;
    
    MinStack() {
        s = new int[capacity];
    }
    
    void push(int val) {
        if(numberOfEntries == capacity){
            capacity *= 2;
            int* tmp = new int[capacity];
            memcpy(tmp, s, sizeof(int) * numberOfEntries);
            swap(tmp, s);
            delete[] tmp;
        }
        s[numberOfEntries++] = val;
        minimum = val < minimum ? val : minimum;
    }
    
    void pop() {
        if(numberOfEntries == 1){
            minimum = INT_MAX;
        }else if(s[numberOfEntries-1] == minimum){
            minimum = s[0];
            for(int i=1;i<numberOfEntries-1;i++){
                minimum = min(s[i],minimum);
            }
        }
        numberOfEntries--;
    }
    
    int top() {
        return s[numberOfEntries-1];
    }
    
    int getMin() {
        return minimum;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
