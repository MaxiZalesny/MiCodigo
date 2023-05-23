/*funcion tiempo parametro en numero ent. llamado total seg y 
tres parametros de referencia enteros nombrados horas min y seg
la funcion es convertir el numero de segundos trasmitido en un num equivalente
de horas min y seg.*/

#include<iostream>
#include<conio.h>
using namespace std;
void tiempo(int,int&,int&,int&);
int main(){
	
	int totalSeg, horas,min,seg;
	
	cout<<"Digite el numero total de segundos: ";
	cin>>totalSeg;
	tiempo(totalSeg,horas,min,seg);
	
    cout<<"\ntiempo equivalente a la cantidad de segundos digitados: "<<endl;
    cout<<"horas: "<<horas<<endl;
    cout<<"min: "<<min<<endl;
    cout<<"seg: "<<seg<<endl;
    
	getch();
    return 0;
}

void tiempo( int totalSeg, int& horas, int& min,int& seg){
	
	horas= totalSeg/3600;
	totalSeg %= 3600;
	min= totalSeg/60;
	seg=totalSeg%60;
}