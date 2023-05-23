//ejemplo de como encontrar el numero maryor

#include<iostream>
#include<conio.h>
using namespace std;

//Prototipo de funcion
int encontrarMax(int x, int y);

int main(){
	int n1,n2;
	int mayor;
	cout<<"Digite 2 numeros: ";
	cin>>n1>>n2;
	mayor = encontrarMax(n1,n2);
	
	cout<<"El mayor de los dos numeros es: "<<mayor<<endl;
	getch();
	return 0;
}
//definicion de funcion
int encontrarMax(int x, int y){
	int numMax;
	
	if(x>y){
		numMax = x;
	
	else{
		numMax = y;
		
	}
	return numMax;
	}
}