#include <iostream>
using namespace std;

int main()
{
    int num = 0;
    int index, days, candles;
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        candles = 0;
        cin >> index >> days;
        for (int j = 2; j < (days + 2); j++)
        {
            candles += j;
        }
        cout << i << ' ' << candles << endl;
    }
    return 0;
}