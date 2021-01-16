#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string line;
    getline(cin, line);

    int N = stoi(line);
    float a = 0.0, b = 0.0, c = 0.0;

    for (int i = 0; i < N; i++)
    {
        getline(cin, line);
        istringstream iss(line);
        for (int j = 0; j < 3; j++)
        {
            float num = 0.0;
            iss >> num;
            if (j == 0)
                a = num;
            if (j == 1)
                b = num;
            if (j == 2)
                c = num;
        }
        if ((a + b) == c)
            cout << "Possible" << endl;
        else if ((a - b) == c || (b - a) == c)
            cout << "Possible" << endl;
        else if ((a * b) == c)
            cout << "Possible" << endl;
        else if ((a / b) == c || (b / a) == c)
            cout << "Possible" << endl;
        else
            cout << "Impossible" << endl;
    }
    return 0;
}