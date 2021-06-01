#include <iostream>
#include <cmath>
#include <string>
using namespace std;

bool is_palindrome(int n)
{
    string s = to_string(n);
    string r = string(s.rbegin(), s.rend());
    return s == r;
}

int solve(int d)
{
    int n = pow(10, d - 1);
    int m = pow(10, d);
    int largest = 0;
    for (int i = n; i < m; i++)
        for (int j = i + 1; j < m; j++) {
            int p = i * j;
            if (largest < p && is_palindrome(p))
                largest = p;
        }
    return largest;
}

int main()
{
    // int d = 2;
    int d = 3;
    cout << solve(d) << endl;
}
