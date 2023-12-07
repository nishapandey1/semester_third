#include <stdio.h>
int main ()
{
int a=1, b=2;
int c;
int sum=0;

while (a <=4000000)
{
    if (a%2 ==0){
        sum += a;
    }
    c=a+b;
    a=b;
    b=c;
}
printf("the sum of even valued fibo terms is: %d\n", sum);
return 0;
}
