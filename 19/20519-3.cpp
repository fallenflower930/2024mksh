#include <iostream>
using namespace std;

int main(){
	int a,i;
	cout<<"��J��Ƽƶq"<<endl;
	cin>>a;
	int b[a];
	cout<<"��J���"<<endl;
	for (i=0;i<=a-1;i++){
		cin>>b[i];
		
	}
 
	for (i=a-1;i>=0;i--){
		
		cout<<b[i]<<" ";
	}
	 
	
	
	
	
	
	return 0;
	
}
