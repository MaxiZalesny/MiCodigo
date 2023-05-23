/*funcion FUNPOt () que eleve un numero entero que se le 
trasmita a una potencia en numeros enteros positivos y despliegue 
el resultado.
El numero entero positivo debera ser el segundo valor trasmitido a la funcion.*/
#include<iostream>
#include<conio.h>
using namespace std;

//prototipo de funciones
void pedirDatos();
void funpot(int x,int y);

int numero,exponente;

int main (){
	pedirDatos();
	funpot(numero,exponente);
	
	getch();
	return 0;
	
}

void pedirDatos(){
	cout<<"Digite un numero: ";
	cin>>numero;
	cout<<"Digite el exponente de elevacion";
	cin>>exponente;
	
}

void funpot(int x ,int y){
	long resultado =1;
	for(int i=1;i<=y;i++){
		resultado *=x;
		
	}
	
	cout<<" EL RESULTADO ES:. " <<funpot<<endl;
}