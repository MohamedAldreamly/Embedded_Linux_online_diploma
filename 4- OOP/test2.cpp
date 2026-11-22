#include <iostream>
using namespace std;

class base;
class B;
class printer
{
public:
    void display(base &b);
    void print(const B &obj);
};

class base
{
private:
    int num1;
    int num2;

public:
    base() {}
    base(int n1, int n2) : num1(n1), num2(n2) {}
    void display()
    {
        cout << "This is base class" << endl;
    }
    friend void show(base &b);
    friend class printer;
};

class B
{
    int a;

public:
    B() {}
    B(int l) : a(l) {}

    friend void printer::print(const B &obj);
};

void show(base &b)
{

    cout << "num1: " << b.num1 << endl;
    cout << "num2: " << b.num2 << endl;
}

void printer::display(base &obj)
{
    cout << obj.num1 << endl;
    cout << obj.num2 << endl;
}

void printer::print(const B &obj)
{
    cout << obj.a << endl;
}

class Counter
{
    int count;

public:
    Counter() : count(0) {}
    Counter(int c) : count(c) {}
    void getCount() const { cout << "Count: " << count << endl; }

    Counter operator+(const Counter &other) const
    {
        return (count + other.count);
    }

    Counter operator-(const Counter &other) const
    {
        return (count - other.count);
    }

    Counter operator*(const Counter &other) const
    {
        return (count * other.count);
    }

    Counter operator<<(int shift) const
    {
        return (count << shift);
    }
};

int main()
{
    // base b{10, 20};
    // B obj{30};
    // // show(b);
    // printer p;
    // p.display(b);
    // p.print(obj);
    Counter c1{10};
    Counter c2{20};
    Counter c3 = c1 + c2;
    Counter c4 = c1 - c2;
    Counter c5 = c1 * c2;
    Counter c6 = c1 << 2;
    Counter c7 = c1 + 20;

    c1.getCount();
    c2.getCount();
    c3.getCount();
    c4.getCount();
    c5.getCount();
    c6.getCount();
    c7.getCount();

    return 0;
}
