#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n)
{
    for (int i = 2; i <= (int)sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}

int solve(int nth)
{
    int n = 2, count = 0;
    while (count < nth) {
        if (is_prime(n))
            count++;
        n++;
    }
    return n - 1;
}

int main()
{
    // int n = 6;
    int n = 10001;
    cout << solve(n) << endl;
}
