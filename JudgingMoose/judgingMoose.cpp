#include <iostream>
using namespace std;

int main()
{
    int l = 0, r = 0;
    cin >> l >> r;
    if (l > r)
        cout << "Odd " << l * 2 << endl;
    else if (r > l)
        cout << "Odd " << r * 2 << endl;
    else if (r == 0 && l == 0)
        cout << "Not a moose" << endl;
    else
        cout << "Even " << l * 2 << endl;

    return 0;
}