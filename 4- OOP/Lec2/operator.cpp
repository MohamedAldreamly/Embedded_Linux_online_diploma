#include <iostream>
using namespace std;

class Counter
{
    int count;

public:
    Counter() : count(0) {}
    Counter(int c) : count(c) {}
    Counter(const Counter &other) : count(other.count) {}

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

    // Overload postfix increment operator
    Counter operator++(int) // int not used just to make compilar understand this post
    {
        Counter temp = *this;
        ++count;
        return temp;
    }
    // Overload prefix increment operator
    Counter &operator++()
    {
        ++count;
        return *this;
    }

    Counter &operator+=(const Counter &other)
    {
        count += other.count;
        return *this;
    }
    Counter &operator-=(const Counter &other)
    {
        count -= other.count;
        return *this;
    }
    Counter &operator*=(const Counter &other)
    {
        count *= other.count;
        return *this;
    }
    Counter &operator/=(const Counter &other)
    {
        count /= other.count;
        return *this;
    }

    Counter &operator<<=(const Counter &other)
    {
        count <<= other.count;
        return *this;
    }

    // Overload copy assignment operator
    // Counter &operator=(const Counter &other)
    // {
    //     if (this == &other) // Check for self-assignment
    //     {
    //         return *this;
    //     }
    //     count = other.count;
    //     return *this;
    // }

    // for move assignment operator
    // Counter &operator=(Counter &&other)
    // {
    //     if (this == &other) // Check for self-assignment
    //     {
    //         return *this;
    //     }
    //     count = other.count;
    //     other.count = 0;
    //     return *this;
    // }

    friend Counter operator+(int x, const Counter &obj);

    void operator()(void)
    {
        cout << "Count: " << count << endl;
    }

    // Overload the extraction operator >>
    friend std::istream &operator>>(std::istream &in, Counter &counter)
    {
        in >> counter.count;
        return in;
    }
    // Overload the insertion operator <<
    friend std::ostream &operator<<(std::ostream &out, const Counter &counter)
    {
        out << counter.count;
        return out;
    }

    void getCount() const { cout << "Count: " << count << endl; }
};

Counter operator+(int x, const Counter &obj)
{
    return Counter(obj.count + x);
}

int main()
{

    Counter c1{10};
    Counter c2{20};

    // Counter c3 = c1 + c2;
    // Counter c4 = c1 - c2;
    // Counter c5 = c1 * c2;
    // Counter c6 = c1 << 2;
    // Counter c7 = c1 + 20;

    // c1.getCount();
    // c2.getCount();
    // c3.getCount();
    // c4.getCount();
    // c5.getCount();
    // c6.getCount();
    // c7.getCount();

    // Copy assignment
    // c2 = c1;

    // Counter c3 = move(c2);
    Counter c3;
    c3 = c1 + c2;
    c3.getCount();
    c3 = c1 + 5;
    c3.getCount();
    c3 = 5 + c2;
    c3.getCount();

    cout << c3;

    return 0;
}
