/*realice una funcion recursiva que calcule un numero elevado a una potencia entera mayor o igual que cero: x^y.

potencia(x,y)=x

  potencia(x,y) = x           ,y=1    
            x*potencia(nx,y-1) ,y>1  
			*/ 
 #include<iostream>
 #include<conio.h>
 using namespace std;
 
 int potencia(int x,int y);
 
 int main(){
 	int base,  exponente;
 	
 
 			cout<<"digite la base: "; cin>>base;
 				cout<<"digite el exponente: "; cin>>exponente;
 		
 		cout<<"\npotencia de "<< base<<" elevado a "<<exponente<<" es:"<<potencia(base,exponente)<<endl;
 		
 	
			 
 	
 	cout<<"\n El resultado es:"<<potencia(base,exponente)<<endl;
 	getch();
 	return 0;
 	
 	
 	
 }
 int potencia(int x, int y){
 	int pot;
 	
 	if(y==1){//caso base
 		pot = x;
 	}
 		
 		else{//caso general
 			pot = x * potencia(x,y-1);
		 }
 		
 		return pot;
	 }
 