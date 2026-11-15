#include <iostream>
template <typename T, int size>
void reverse_array(T arr[])
{
    T L_index = size - 1;
    int i;
    T temp;

    for (i = 0; i < (size / 2); i++)
    {
        temp = arr[i];
        arr[i] = arr[L_index];
        arr[L_index] = temp;
        L_index--;
    }

    if ((L_index - i < 1))
    {
        return;
    }
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6};
    reverse_array<int, 6>(arr);
    for (auto num : arr)
    {
        std::cout << num;
    }
    return 0;
}