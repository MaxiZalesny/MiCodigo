#include<iostream>
 #include<conio.h>

 using namespace std;
 
 
 void pedirDatos();
 char nombreUsuario[30];

int contandoVocales(char *);

 
 int main(){
 	
 	pedirDatos();
 	cout<<"\nEl numero de vocales es: "<<contandoVocales(nombreUsuario)<<endl;


 	getch();
 	return 0;
 	
 } 
 void pedirDatos(){
 	
 	cout<<"digite su nombre: "; 
 	cin.getline(nombreUsuario,30,'\n');
	 	
 	strupr(nombreUsuario);
 	
 }
 
 int contandoVocales (char *nombre){
 	
 	int cont=0;
 	
 	while(*nombre){
 		
 		
 		switch(*nombre){
 			case 'A':
 		    case 'E':
 		   	case 'I':
 		   	case 'O':
 		   	case 'U': cont++;
		 }
		 nombre++;
	 }
	 	return cont;
}

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 