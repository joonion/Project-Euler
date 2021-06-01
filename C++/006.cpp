#include <iostream>
#include <cmath>
using namespace std;

int solve(int n)
{
    int s1 = n * (n + 1) * (2 * n + 1) / 6;
    int s2 = pow(n * (n + 1) / 2, 2);
    return s2 - s1;
}

int main()
{
    // int n = 10;
    int n = 100;
    cout << solve(n) << endl;
}
