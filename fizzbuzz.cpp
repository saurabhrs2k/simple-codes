#include<iostream>
#include<string.h>

using namespace std;

int main()
{
   int c3 = 0;
   int c5 = 0;
   string output = "";
   for(int x = 1; x <= 100; x++){
        c3+=1;
        c5+=1;
        output = "";
        if(c3 == 3){
            output += "Fizz";
            c3 = 0;}
        if(c5 == 5){
            output += "Buzz";
            c5 = 0;}
        if(output == ""){
         output += to_string(x);}
        cout<<output<<endl;
}
}