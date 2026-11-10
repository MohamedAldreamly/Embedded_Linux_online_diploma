#include <iostream>
using namespace std;

int reverse(int x)
{
    static int reversed = 0;

    if (x < 0)
    {
        return 0;
    }

    if (x == 0)
    {
        return reversed;
    }

    int digit = x % 10;

    reversed = reversed * 10 + digit;

    return reverse(x / 10);
}

int main()
{

    int number;
    cout << "Input: x =" << endl;
    cin >> number;

    cout << "Input: x = " << number << endl;

    int reversedNumber = reverse(number);
    if (reversedNumber == number)
    {
        cout << "Output: true" << endl;
        cout << "Explanation: " << number << " reads as " << number << " from left to right and from right to left." << endl;
    }
    else if (number < 0)
    {
        cout << "Output: false" << endl;
        int x = number * -1;
        cout << "Explanation: From left to right, it reads " << x << "-. From right to left, it becomes " << x << "-. Therefore it is not a palindrome." << endl;
    }
    else
    {
        cout << "Output: false" << endl;
        cout << "Explanation: Reads " << reversedNumber << " from right to left. Therefore it is not a palindrome." << endl;
    }

    return 0;
}