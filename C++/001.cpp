#include <iostream>
using namespace std;

int solve(int n)
{
    int s = 0;
    for (int i = 1; i < n; i++)
        if (i % 3 == 0 || i % 5 == 0)
            s += i;
    return s;
}

int main()
{
    // int n = 10;
    int n = 1000;
    cout << solve(n) << endl;
}
