/*realice una funcion recursiva que sume los primeros n enteros positivos 
nota: para plantear la funcion recursiva tenga en cuenta que la suma puede expresarse 
mediante la siguiente recurencia:

  suma(n) = 1           ,si n=1    
            n+suma(n-1) ,si>1  
			*/ 
 #include<iostream>
 #include<conio.h>
 using namespace std;
 
 int sumar(int);
 
 int main(){
 	int nElementos;
 	
 	do{
 			cout<<"digite el numero de elementos: ";
 			cin>>nElementos;
 		}while(nElementos <=0);
			 
 	
 	cout<<"\nLa suma es:"<<sumar(nElementos)<<endl;
 	getch();
 	return 0;
 	
 	
 	
 }
 int sumar(int n){
 	int suma = 0;
 	
 	if(n==1){//caso base
 		suma = 0;
 	}
 		
 		else{//caso general
 			suma = n+sumar(n-1);
		 }
 		
 		
	 }
 