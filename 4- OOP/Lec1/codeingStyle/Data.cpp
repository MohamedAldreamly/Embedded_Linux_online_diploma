#include "Data.hpp"
#include <iostream>

Data::Data() : num1(0), num2(0)
{
}

Data::Data(int a, int b)
    : num1(a), num2(b)
{
}

void Data::print() const
{
    std::cout << num1 << " "
              << num2 << std::endl;
}

void Data::setNum1(int value)
{
    num1 = value;
}