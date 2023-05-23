 /*Transmision de Direcciones
 
 ejemplo: Intercambiar el valor de 2 variables. */
 
 #include<iostream>
 #include<conio.h>

 using namespace std;
 
 //Prototipo de Funcion
 
 void intercambio(float*,float*);//prototipo
 
 int main(){
 	float num1 = 20.8, num2 = 6.31;
 	
 	cout<<"Primer numero:"<<num1<<endl;
 		cout<<"Segundo numero:"<<num2<<endl;
 		 
		  intercambio(&num1,&num2);//llamo a la funcion intercambio
		  
		    cout<<"\n\nDespues del intercambio: \n\n ";
 	      	cout<<"El nuevo valor de num 1: "<<num1<<endl;
 	      	cout<<"El nuevo valor de num 2: "<<num2<<endl;
 		
		 getch();
 		return 0;
 		
 		
 	
 }
 void intercambio(float *dirNm1,float *dirNm2){
 	float aux;
 	
 	//Intercambiar los valores de las variables
 	
 	aux = *dirNm1;
 	*dirNm1 = *dirNm2;
 	*dirNm2 = aux;
 }