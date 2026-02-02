#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const long long number = 600851475143;

const long long limit = sqrt(number)+1;
// const long long limit = 10;

vector<long long> sieve(long long limit){
    vector<bool> isPrime(limit+1, true);
    isPrime[0] = isPrime[1] = false;
    for (long long i=2; i*i<limit; i++){
        if (isPrime[i]){
            for (long long j = i*i; j<limit; j+=i){
                isPrime[j] = false;
            }
        }
    }

    vector<long long> primes;

    for (long long i = 2; i < limit; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

vector<long long> factors(long long number, vector<long long> primes){
    vector<long long> factors;
    for (long long prime: primes){
        if (number%prime == 0){
            factors.push_back(prime);
        }
    }
    return factors;
}

int main(){
    vector<long long> primes = sieve(limit);
    vector<long long> factor_list = factors(number, primes);
    cout << factor_list[factor_list.size()-1] << endl;
}