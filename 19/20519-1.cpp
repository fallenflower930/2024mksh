#include <iostream>
using namespace std;

int main(){
	int m,c;
	float km;
	cout<<"��J������"<<endl;
	cin>>km;

	if (km > 1){
		m = km*1000;
		c = (m-1000)/500;
	   	if ((m-1000)%500 != 0)
			c++;
	}
	
	cout <<"���I"<<65+c*5<<"��"<<endl; 
	
	
	
	
	
	
	
}
