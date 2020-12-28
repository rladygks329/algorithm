#include<iostream>
using namespace std;
int main(){
  char a[4],b[4];
  char temp;
  cin >> a >> b;

  temp = a[0];
  a[0] = a[2];
  a[2] = temp;

  temp = b[0];
  b[0] = b[2];
  b[2] = temp;

  for(int i=0;i<3;i++)
  {
    if(a[i] < b[i]) {cout << b; break;}
    else if(a[i] == b[i]) continue;
    else {cout << a; break;}
  }
  return 0;
}
