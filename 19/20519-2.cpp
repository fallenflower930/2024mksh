#include <iostream>
using namespace std;

int main(){
	int a,b;
	cout<<"輸入1數"<<endl;
	cin>>a;
	cout<<a<<"的因數有:"; 
    for(b=1;b<= a;b++){
    	if (a%b ==0)
        	cout<<b<<" ";
}
	return 0;
	
	
	
	
	
	
	
}
