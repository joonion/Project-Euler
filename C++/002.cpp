#include <iostream>
using namespace std;

int solve(int n)
{
    int a = 1, b = 2, s = 0;
    while (b <= n) {
        int t = a + b;
        a = b;
        b = t;
        if (a % 2 == 0)
            s += a;
    }
    return s;
}

int main()
{
    int n = 4000000;
    cout << solve(n) << endl;
}
