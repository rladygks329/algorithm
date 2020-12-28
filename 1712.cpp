#include<iostream>
using namespace std;
int main(){
  int fixed_cost, flexible_cost, product_cost;
  cin >> fixed_cost >> flexible_cost >> product_cost;

  int bep = 0;
  if (flexible_cost < product_cost)
  {
    cout << fixed_cost/(product_cost - flexible_cost) +1 <<endl;
  }
  else
    cout << -1 << endl;


  return 0;
}
