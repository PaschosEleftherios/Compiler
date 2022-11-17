#include <stdio.h>

int main()
{
	int x,sum,average,count,T_1,T_2,T_3;
	L_1:  //(begin_block,average,_,_)
	L_2: scanf("x= %d",&x);
	L_3: sum=0; //(:=,0,_,sum)
	L_4: count=0; //(:=,0,_,count)
	L_5: if (x>1) goto L_7; //(>,x,1,7)
	L_6: goto L_12; //(jump,_,_,12)
	L_7: T_1=sum+x; //(+,sum,x,T_1)
	L_8: sum=T_1; //(:=,T_1,_,sum)
	L_9: T_2=count+1; //(+,count,1,T_2)
	L_10: count=T_2; //(:=,T_2,_,count)
	L_11: goto L_5; //(jump,_,_,5)
	L_12: T_3=sum/count; //(/,sum,count,T_3)
	L_13: average=T_3; //(:=,T_3,_,average)
	L_14: printf("average= %d", average);
	L_15: //(halt,_,_,_)
} 
	