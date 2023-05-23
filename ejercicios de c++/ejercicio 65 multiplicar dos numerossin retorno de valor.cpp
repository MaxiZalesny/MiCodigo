/*funcion FUNPOt () que eleve un numero entero que se le 
trasmita a una potencia en numeros enteros positivos y despliegue 
el resultado.
El numero entero positivo debera ser el segundo valor trasmitido a la funcion.*/
#include<iostream>
#include<conio.h>
using namespace std;

//prototipo de funciones
void pedirDatos();
void mult(float x,float y);

int num1,num2;

int main (){
	pedirDatos();
	mult(num1,num2);
	
	getch();
	return 0;
	
}

void pedirDatos(){
	cout<<"Digite 2 numeros: ";
	cin>>num1>>num2;

	
}

void mult(float x ,float y){
float multiplicacion = x * y;
		
	
	
	cout<< "La multiplicacion es : " <<multiplicacion<<endl;
}