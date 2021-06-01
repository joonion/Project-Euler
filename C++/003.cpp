#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned long long LongInt;

LongInt solve(LongInt n)
{
    for (int i = 2; i <= (int)sqrt(n); i ++)
        if (n % i == 0)
            return solve(n / i);
    return n;
}

int main()
{
    // LongInt n = 13195;
    LongInt n = 600851475143;
    cout << solve(n) << endl;
}
