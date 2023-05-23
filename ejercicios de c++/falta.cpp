 /*Asignacion dinamica de arreglos
 new :recerva el numero de bytes solocitado por la declaracion.
 delete : Libera un bloque de bytes recervado con anterioridad.
 
 EJEMPLO: Pedir al usuario n calificaciones y almacenarlos en un arreglo dinamico*/
 
 #include<iostream>
 #include<conio.h>
 #include<stdlib.h>//Funciona new y delete
 using namespace std;
 
 //Prototipo de Funcion
 
 void pedirNotas();
 void mostrarNotas();
 int numCalif,*calif;
 
 int main(){
 	
 	pedirNotas();
 	mostrarNotas();
 	delete[]calif;//liberando el espacio en bytes utilizados anteriormente
 	
 	getch();
 	return 0;
 }
 void pedirNotas(){
 	cout<<"Digite el numero de calificaciones: ";
 	cin>>numCalif;
 	
 	calif = new int[numCalif];//crear el arreglo
 	
 	for(int i=0;i<numCalif;i++){
 		cout<<"Ingrese una nota: ";
 		cin>>calif[i];
		 }
 		
	 }
 	
 	void mostrarNotas(){
 		cout<<"\n\nMostrando notas del usuario:\n";
 		for(int i =0;i<numCalif;i++){
 			cout<<calif[i]<<endl;
			 }
		 }
	 
 