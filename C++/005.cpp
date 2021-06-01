#include <iostream>
using namespace std;

typedef unsigned long long LongInt;

LongInt gcd(LongInt n, LongInt m)
{
    if (m == 0)
        return n;
    else 
        return gcd(m, n % m);    
}

LongInt lcm(LongInt n, LongInt m)
{
    return n * m / gcd(n, m);
}

LongInt solve(LongInt n)
{
    LongInt m = 1;
    for (LongInt i = 2; i <= n; i++)
        m = lcm(m, i);
    return m;
}

int main()
{
    // int n = 10;
    int n = 20;
    cout << solve(n) << endl;
}
