#include <iostream>
using namespace std;

int main()
{
    int num = 0;
    int stripNum = 0;
    int stripSize = 0;
    int totalStrips = 0;

    cin >> num;

    for (int i = 0; i < num; i++)
    {
        // Get number of Strips
        cin >> stripNum;
        int j = 0;
        // All connecting stripns and available outlets.
        while (j != (stripNum - 1))
        {
            cin >> stripSize;
            totalStrips += (stripSize - 1);
            j++;
        }
        // Last Strip has all available
        cin >> stripSize;
        totalStrips += stripSize;

        cout << totalStrips << endl;
        totalStrips = 0;
    }
    return 0;
}