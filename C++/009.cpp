#include <iostream>
using namespace std;

int solve(int n)
{
    int a, b, c;
    for (a = 1; a < n; a++)
        for (b = a + 1; b < n; b++) {
            c = n - a - b;
            if (a * a + b * b == c * c)
                return a * b * c;
        }
    return 0;
}

int main()
{
    int n = 1000;
    cout << solve(n) << endl;
}