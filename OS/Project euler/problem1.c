#include <stdio.h>

int main ()
{
int i;
int a=1000;
int sum=0;
for (i=1;i<a;i++)
{
    if (i%3==0 || i%5==0) {
        sum=sum+i;
    }
}
printf("The sum is: %d\n",sum);
return 0;
}
