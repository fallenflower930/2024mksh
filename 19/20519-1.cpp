#include <iostream>
using namespace std;

int main(){
	int m,c;
	float km;
	cout<<"輸入公里數"<<endl;
	cin>>km;

	if (km > 1){
		m = km*1000;
		c = (m-1000)/500;
	   	if ((m-1000)%500 != 0)
			c++;
	}
	
	cout <<"應付"<<65+c*5<<"元"<<endl; 
	
	
	
	
	
	
	
}
