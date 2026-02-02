#include <iostream>
int sum = 0;

int main(){

    for(int i=0; i<1000; i++){
        if(i%3 == 0 || i%5 == 0){
            sum += i;
        }
    }

    std::cout << sum << std::endl;

    // or for number, not sum

    int sum2 = 1000/3 + 1000/5 - 1000/15;

    std::cout << sum2 << std::endl;

} 