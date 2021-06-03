#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long LongInt;

LongInt solve(LongInt n)
{
    vector<bool> sieve(n + 1, true);
    LongInt sum = 0;
    for (int i = 2; i <= n; i++)
        if (sieve[i] == true) {
            sum += i;
            for (int j = i + i; j <= n; j += i) 
                sieve[j] = false;
        }
    return sum;
}

int main()
{
    // int n = 10;
    int n = 2000000;
    cout << solve(n) << endl;
}