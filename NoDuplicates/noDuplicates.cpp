#include <iostream>
#include <cstring>
#include <iterator>
#include <vector>
using namespace std;

int kattis()
{
    string line;
    getline(cin, line);

    string tempS = "";
    vector<string> words;

    for (char const &ch : line)
    {
        if (ch == ' ')
        {
            words.push_back(tempS);
            tempS = "";
        }
        else
            tempS += ch;
    }
    words.push_back(tempS);
    vector<string>::iterator it, it2;
    for (it = words.begin(); it < words.end(); it++)
    {
        for (it2 = next(it, 1); it2 < words.end(); it2++)
        {
            if (*it == *it2)
            {
                cout << "no" << endl;
                return 0;
            }
        }
    }
    cout << "yes" << endl;
    return 0;
}
void test()
{
    cout << "test" << endl;
}

int main(int argc, char *argv[])
{
    if (argc > 1 && strncmp(argv[1], "test", 4) == 0)
        test();
    else
        kattis();
    return 0;
}
