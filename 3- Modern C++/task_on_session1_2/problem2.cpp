#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <math.h>

bool isAlienSorted(vector<string> &words, string order)
{
    long long unsigned int num_order = order.length();
    long long unsigned int num_word1 = words[0].size();
    long long unsigned int num_word2 = words[1].size();
    unsigned int i;
    unsigned int j;
    unsigned int pos1;
    unsigned int pos2;
    for (j = 0; j < min(num_word1, num_word2); j++)
    {
        if (words[0][j] == words[1][j])
        {
            continue;
        }
        else
        {
            for (i = 0; i < num_order; i++)
            {
                if (order[i] == words[0][j])
                {
                    pos1 = i;
                }
            }
            for (i = 0; i < num_order; i++)
            {
                if (order[i] == words[1][j])
                {
                    pos2 = i;
                }
            }

            if (pos1 < pos2)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
    if (num_word1 <= num_word2)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    vector<string> words(2);
    string order;

    cout << "Input words and order:" << endl;
    cin >> words[0] >> words[1];
    cin >> order;

    if (isAlienSorted(words, order))
    {
        cout << "Output: true" << endl;
        cout << "Explanation: The words are sorted according to the given alien dictionary order." << endl;
    }
    else
    {
        cout << "Output: false" << endl;
        cout << "Explanation: The words are not sorted according to the given alien dictionary order." << endl;
    }
}