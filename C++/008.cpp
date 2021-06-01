#include <iostream>
#include <string>
using namespace std;

typedef unsigned long long LongInt;

LongInt solve(string s, int n)
{
    LongInt product = 0, greatest = 0;
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        product *= (int)(s[i] - '0');
        if (product == 0) {
            product = (int)(s[i] - '0');
            start = end = i;
        }
        else {
            if (end - start + 1 < n)
                end++;
            else {
                start++; end++;
                product /= (int)(s[start - 1] - '0');
            }
        }
        if (greatest < product)
            greatest = product;
    }
    return greatest;
}

int main()
{
    string s, t;
    for (int i = 0; i < 20; i++) {
        cin >> t;
        s += t;
    }
    // int n = 4;
    int n = 13;
    cout << solve(s, n) << endl;
}
