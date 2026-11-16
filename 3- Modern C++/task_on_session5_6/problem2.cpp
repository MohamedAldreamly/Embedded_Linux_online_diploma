#include <iostream>
#include <vector>

template <typename T>
void rotate_left_by_position(std::vector<T> &vec, int order)
{
    int i;
    T val;

    for (i = 0; i < (order); i++)
    {
        val = vec.front();
        vec.erase(vec.begin());
        vec.push_back(val);
    }
}

int main()
{
    std::vector<int> vec;
    int val;
    for (int i = 0; i < 10; i++)
    {
        std::cout << "Enter Number " << i + 1 << " : ";
        std::cin >> val;
        std::cout << std::endl;
        vec.push_back(val);
    }
    std::cout << "Enter the Number of Rotation: ";
    std::cin >> val;
    std::cout << std::endl;

    std::cout << "Orignal array: ";
    for (auto num : vec)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    rotate_left_by_position<int>(vec, val);
    std::cout << "array after rotating left by " << val << " positions : ";

    for (auto num : vec)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}