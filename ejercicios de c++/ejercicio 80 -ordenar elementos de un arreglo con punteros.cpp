 #include<iostream>
 #include<conio.h>
 #include<stdlib.h> //new y delete
 using namespace std;
 //prot de fun
 void pedirDatos();
 void ordenarArreglo(int*,int);
 void mostrarArreglo(int*,int);
 int nElemetos, *elemento;
 
 int main(){
 	 pedirDatos();
 	ordenarArreglo(elemento,nElementos);
 	mostrarArreglo(elemento,nElemento);
 	delete[]elemento;
 	getch();
 	return0;
 	
 	
 }
 
 void pedirDatos(){
 	cout<<"Digite el numero de elementos del Arreglo: ";
 	cin>>nElementos;
 	
 	elemento = new int[nElemento]
 	
 	for (int i=0;i<nElementos;i++){
 		
 		cout<<"Digite un numero["<<i<<"]: ";
 		cin>>*(elemento+i);//elemento[i]
	 }
 	
 }
 
 void ordenarArreglo(int *elemento,int nElemento){
 	
 int aux;
 
 for(int i=0;i<nElementos;i++){
  for(int j=0;j<nElementos-1;j++){
  	if(*(elemento+j) > *(elemento+j+1)){
  		aux = *(elemento+j);
  		*(elemento+j) = *(elemento+j+1);
  		*(elemento+j+1) = aux;
	  }
  } 
  }	
 	
 	
 }
 void mostrarArreglo(int *elemento,int nElemento){
 	cout<<"\n\nMostrando arreglo ordenado: ";
 	for(int i=0;i<nElemento;i++){
 		cout<<*(elemento+i);
	 }
 	
 }