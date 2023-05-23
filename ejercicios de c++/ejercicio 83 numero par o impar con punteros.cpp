/*ejercicio 1 de punteros , comprobar si un numero es par o impar y
 señalar la posicion de memoria donde se este guardando el numero.con puntreros.*/
 
 
 #include<iostream>
 #include<conio.h>
 using namespace std;
 
 int main(){
 	 int numero, *dir_numero;
	  
	  cout<<"Digite un numero: ";cin>>numero;
	  
	  dir_numero = &numero; //GUARDANDO LA POS DE MEMORIA
	  
	  if (*dir_numero%2==0){
	  	 cout<<"el numero"<<*dir_numero<<" es par"<<endl;
	  	 cout<<"Posicion:"<<dir_numero<<endl;
	  	 }
	  	 else{
	  	 	cout<<"El numero "<<*dir_numero<<"es impar"<<endl;
	  	 	cout<<"Posicion: "<<dir_numero<<endl;
		   }
	     getch();
	     return 0;
	  }
	  
 	 
 	 
 	 
 	 
 	 
 	 