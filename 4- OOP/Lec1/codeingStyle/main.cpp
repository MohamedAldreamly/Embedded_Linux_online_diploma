#include "Data.hpp"

int main()
{
    Data obj1;
    Data obj2(10, 20);

    obj1.setNum1(50);

    obj1.print();
    obj2.print();

    return 0;
}