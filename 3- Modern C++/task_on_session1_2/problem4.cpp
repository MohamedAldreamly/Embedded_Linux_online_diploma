#include <iostream>
using namespace std;

int max(int arr[])
{
    unsigned int i;
    int max = arr[0];
    for (i = 1; i < 5; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max;
}

int main()
{
    int arr[5];
    cout << "Enter the elements of the array: ";
    cout << endl;

    unsigned int i;
    for (i = 0; i < 5; i++)
    {
        cin >> arr[i];
    }

    int maximum = max(arr);
    cout << "The maximum element in the array is: " << maximum << endl;

    return 0;
}