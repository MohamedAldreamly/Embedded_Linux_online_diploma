#include <iostream>
using namespace std;

class Box; // Forward declaration

class Printer
{
public:
    void printVolume(Box &box);
};

class Box
{
private:
    double length;
    double breadth;
    double height;
    // Friend class declaration
    friend class Printer;

public:
    Box(double l, double b, double h) : length(l), breadth(b), height(h) {}
};

void Printer::printVolume(Box &box)
{
    double volume = box.length * box.breadth * box.height;
    cout << "Volume of the box: " << volume << endl;
}

class B;
class A
{
public:
    void display(const B &obj);
};
class B
{
    int a;

public:
    B() {}
    B(int A) : a(A) {}
    friend void A::display(const B &obj);
};

void A::display(const B &obj)
{
    cout << obj.a << endl;
}

int main()
{
    Box box(3.0, 4.0, 5.0);
    Printer printer;
    printer.printVolume(box);

    A objA;
    B objB(10);
    objA.display(objB);

    return 0;
}
