#include <iostream>
#include <cstdlib>

using namespace std;
int bul(int n,int m)
{
if(n-1==m)
    return 1;
    if(n%m==0)
    return 0;

    return bul(n,m+1);
}

int gonder(int n){
    if(bul(n,2))
        return n;
return gonder(n-1);

}
int main()
{int a;
    cout << "sayiyi giriniz" << endl;
  cin>>a;
  cout << a <<"dan kucuk en buyuk asal sayı = " ;
  cout<<gonder(a)<<endl;
  cin>>a;
    return 0;
}
