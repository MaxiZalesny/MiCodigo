//paso de parametro de tipo estructura

#include<iostream>
#include<conio.h>
using namespace std;

struct Persona{
	char nombre[30];
	int edad;
	
}p1;
//prototipo
void pedirDatos();
void mostrarDatos(Persona);

int main(){
	pedirDatos();
	mostrarDatos(p1);
	
	
	 getch();
	 return 0;
	 
	
}
void pedirDatos(){
	cout<<"Digite su nombre: ";
	cin.getline(p1.nombre,30, '\n')	;
	cout<<"Digite su edad: ";
	cin>>p1.edad;
}
void mostrarDatos(Persona p){
	cout<<"\n\nombre: "<<p.nombre<<endl;
	cout<<"Edad: "<<p.edad<<endl;
}